#!/usr/bin/env python3
from __future__ import annotations

import fcntl
import json
import os
import shlex
import subprocess
from contextlib import contextmanager
from pathlib import Path
from typing import Any, Iterator, Mapping

DEFAULT_SUBPROCESS_TIMEOUT_SECONDS = 120.0
DEFAULT_TAIL_CHARS = 1000
DEFAULT_JSON_DICT_TIMEOUT_SECONDS = DEFAULT_SUBPROCESS_TIMEOUT_SECONDS


class AutomationRuntimeError(RuntimeError):
    pass


class AutomationLockError(AutomationRuntimeError):
    pass


def tail_text(value: Any, *, limit: int = DEFAULT_TAIL_CHARS) -> str:
    text = str(value or '')
    if len(text) <= limit:
        return text
    return text[-limit:]


def command_preview(cmd: list[str]) -> str:
    return shlex.join([str(part) for part in cmd])


def parse_json_output(stdout: str) -> dict[str, Any]:
    text = (stdout or '').strip()
    if not text:
        return {}
    candidates = [text]
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    if lines:
        candidates.extend(reversed(lines))
    for candidate in candidates:
        try:
            payload = json.loads(candidate)
        except json.JSONDecodeError:
            continue
        if isinstance(payload, dict):
            return payload
    return {}


def run_subprocess(
    cmd: list[str],
    *,
    cwd: str | Path | None = None,
    env: Mapping[str, str] | None = None,
    input_text: str | None = None,
    timeout_seconds: float = DEFAULT_SUBPROCESS_TIMEOUT_SECONDS,
) -> subprocess.CompletedProcess[str]:
    try:
        return subprocess.run(
            cmd,
            cwd=str(cwd) if cwd is not None else None,
            env=dict(env) if env is not None else None,
            input=input_text,
            text=True,
            capture_output=True,
            timeout=timeout_seconds,
            check=False,
        )
    except subprocess.TimeoutExpired as exc:
        stdout = tail_text(exc.stdout)
        stderr = tail_text(exc.stderr)
        detail = f'command timed out after {timeout_seconds:.1f}s: {command_preview(cmd)}'
        if stdout:
            detail += f'\nstdout_tail={stdout}'
        if stderr:
            detail += f'\nstderr_tail={stderr}'
        raise AutomationRuntimeError(detail) from exc


def run_json_subprocess(
    cmd: list[str],
    *,
    cwd: str | Path | None = None,
    env: Mapping[str, str] | None = None,
    input_text: str | None = None,
    timeout_seconds: float = DEFAULT_SUBPROCESS_TIMEOUT_SECONDS,
) -> tuple[subprocess.CompletedProcess[str], dict[str, Any]]:
    proc = run_subprocess(cmd, cwd=cwd, env=env, input_text=input_text, timeout_seconds=timeout_seconds)
    return proc, parse_json_output(proc.stdout or '')


@contextmanager
def exclusive_lock(
    path: Path,
    *,
    bypass_env_var: str = '',
    blocking: bool = False,
    error_message: str | None = None,
) -> Iterator[Path]:
    if bypass_env_var and os.getenv(bypass_env_var):
        yield path
        return

    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('a+', encoding='utf-8') as handle:
        flags = fcntl.LOCK_EX if blocking else (fcntl.LOCK_EX | fcntl.LOCK_NB)
        try:
            fcntl.flock(handle.fileno(), flags)
        except BlockingIOError as exc:
            raise AutomationLockError(error_message or f'another process already holds {path}') from exc
        try:
            handle.seek(0)
            handle.truncate()
            handle.write(str(os.getpid()))
            handle.flush()
            yield path
        finally:
            fcntl.flock(handle.fileno(), fcntl.LOCK_UN)


def load_json_dict(path: Path, *, artifact_name: str, required_keys: list[str] | None = None) -> dict[str, Any]:
    if not path.exists():
        raise AutomationRuntimeError(f'{artifact_name} does not exist: {path}')
    try:
        payload = json.loads(path.read_text())
    except Exception as exc:  # noqa: BLE001
        raise AutomationRuntimeError(f'{artifact_name} is not valid JSON: {path}') from exc
    if not isinstance(payload, dict):
        raise AutomationRuntimeError(f'{artifact_name} must contain a top-level JSON object: {path}')
    missing = [key for key in (required_keys or []) if key not in payload]
    if missing:
        raise AutomationRuntimeError(f'{artifact_name} is missing required keys {missing}: {path}')
    return payload
