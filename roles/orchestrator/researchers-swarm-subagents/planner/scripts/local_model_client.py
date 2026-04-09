#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import urllib.error
import urllib.request


def _extract_json_object(text: str) -> dict:
    text = text.strip()
    if not text:
        raise RuntimeError("empty model text")

    # direct parse
    try:
        parsed = json.loads(text)
        if isinstance(parsed, dict):
            return parsed
    except json.JSONDecodeError:
        pass

    # fenced block or surrounding text
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if match:
        candidate = match.group(0)
        try:
            parsed = json.loads(candidate)
            if isinstance(parsed, dict):
                return parsed
        except json.JSONDecodeError:
            pass

    raise RuntimeError("ollama model response was not valid JSON")


def ollama_generate(*, endpoint: str, model: str, prompt: str, timeout_seconds: float = 8.0) -> dict:
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False,
        "format": "json",
        "think": False,
    }
    req = urllib.request.Request(
        endpoint.rstrip("/") + "/api/generate",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout_seconds) as resp:
            body = resp.read().decode("utf-8")
    except urllib.error.URLError as exc:
        raise RuntimeError(f"ollama request failed: {exc}") from exc

    try:
        payload = json.loads(body)
    except json.JSONDecodeError as exc:
        raise RuntimeError("ollama returned non-JSON response") from exc

    response_text = payload.get("response")
    if isinstance(response_text, str) and response_text.strip():
        return _extract_json_object(response_text)

    thinking_text = payload.get("thinking")
    if isinstance(thinking_text, str) and thinking_text.strip():
        return _extract_json_object(thinking_text)

    raise RuntimeError(f"ollama response field missing or empty; raw keys={sorted(payload.keys())}")


def ollama_tags(*, endpoint: str, timeout_seconds: float = 3.0) -> dict:
    req = urllib.request.Request(endpoint.rstrip("/") + "/api/tags", method="GET")
    try:
        with urllib.request.urlopen(req, timeout=timeout_seconds) as resp:
            body = resp.read().decode("utf-8")
    except urllib.error.URLError as exc:
        raise RuntimeError(f"ollama tags request failed: {exc}") from exc

    try:
        return json.loads(body)
    except json.JSONDecodeError as exc:
        raise RuntimeError("ollama tags response was not valid JSON") from exc
