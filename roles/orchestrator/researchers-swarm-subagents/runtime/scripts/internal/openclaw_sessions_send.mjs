#!/usr/bin/env node
import { pathToFileURL } from 'node:url';

const callMod = await import(pathToFileURL('/opt/homebrew/lib/node_modules/openclaw/dist/call-CQbSO4Fr.js').href);
const msgMod = await import(pathToFileURL('/opt/homebrew/lib/node_modules/openclaw/dist/message-channel-BliByQBl.js').href);

const callGateway = callMod.r;
const GATEWAY_CLIENT_NAMES = msgMod.h;
const GATEWAY_CLIENT_MODES = msgMod.m;

function parseArgs(argv) {
  const args = [...argv];
  let payloadJson = '';
  for (let i = 0; i < args.length; i += 1) {
    const arg = args[i];
    if (arg === '--payload-json') {
      payloadJson = args[i + 1] ?? '';
      i += 1;
    }
  }
  if (!payloadJson.trim()) {
    throw new Error('Missing required --payload-json <json>');
  }
  return { payloadJson };
}

function normalizePayload(raw) {
  const sessionKey = typeof raw.sessionKey === 'string' ? raw.sessionKey.trim() : '';
  const message = typeof raw.message === 'string' ? raw.message : '';
  const timeoutSeconds = typeof raw.timeoutSeconds === 'number' && Number.isFinite(raw.timeoutSeconds)
    ? raw.timeoutSeconds
    : undefined;
  const timeoutMs = timeoutSeconds !== undefined ? Math.max(0, Math.floor(timeoutSeconds * 1000)) : undefined;
  const agentId = typeof raw.agentId === 'string' && raw.agentId.trim() ? raw.agentId.trim() : undefined;

  if (!sessionKey) throw new Error('payload.sessionKey is required');
  if (!message.trim()) throw new Error('payload.message is required');

  return {
    key: sessionKey,
    message,
    ...(timeoutMs !== undefined ? { timeoutMs } : {}),
    ...(agentId ? { agentId } : {}),
  };
}

async function gatewayCall(method, params, timeoutMs) {
  return await callGateway({
    method,
    params,
    timeoutMs,
    mode: GATEWAY_CLIENT_MODES.CLI,
    clientName: GATEWAY_CLIENT_NAMES.CLI,
    clientDisplayName: 'OpenClaw CLI',
  });
}

async function main() {
  const { payloadJson } = parseArgs(process.argv.slice(2));
  const raw = JSON.parse(payloadJson);
  const params = normalizePayload(raw);
  await gatewayCall('sessions.create', { key: params.key }, 8000);
  const result = await gatewayCall(
    'sessions.send',
    params,
    Math.max(5000, typeof params.timeoutMs === 'number' ? params.timeoutMs + 5000 : 25000),
  );
  process.stdout.write(JSON.stringify(result));
}

main().catch((err) => {
  process.stderr.write(`${String(err)}\n`);
  process.exit(1);
});
