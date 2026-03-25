#!/bin/zsh
set -euo pipefail

CHROME_APP="/Applications/Google Chrome.app"
CHROME_BIN="$CHROME_APP/Contents/MacOS/Google Chrome"
PROFILE_ROOT="$HOME/Library/Application Support/Google/Chrome"
PORT_FILE="$PROFILE_ROOT/DevToolsActivePort"

if [ ! -x "$CHROME_BIN" ]; then
  echo "Chrome not found at $CHROME_BIN" >&2
  exit 1
fi

# Launch the normal user Chrome app if it is not already running.
if ! pgrep -f "^/Applications/Google Chrome.app/Contents/MacOS/Google Chrome$" >/dev/null 2>&1; then
  open -a "$CHROME_APP"
fi

# Wait for the remote debugging attach point to appear.
for i in {1..30}; do
  if [ -f "$PORT_FILE" ]; then
    echo "user_chrome_debug=ready"
    echo "devtools_file=$PORT_FILE"
    exit 0
  fi
  sleep 1
done

echo "Timed out waiting for Chrome debug attach point: $PORT_FILE" >&2
exit 2
