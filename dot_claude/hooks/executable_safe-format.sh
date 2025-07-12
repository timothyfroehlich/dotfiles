#!/bin/bash

# Safe auto-formatting hook for Claude Code
# Avoids infinite loops by checking for lock files and timeouts

LOCK_FILE="/tmp/claude-formatting.lock"
TIMEOUT=5

# Exit if already formatting (prevent infinite loops)
if [ -f "$LOCK_FILE" ]; then
    exit 0
fi

# Create lock file
touch "$LOCK_FILE"

# Clean up lock file on exit
cleanup() {
    rm -f "$LOCK_FILE"
}
trap cleanup EXIT INT TERM

# Only format if we're in a project with package.json (Node.js project)
if [ ! -f "package.json" ]; then
    exit 0
fi

# Check if prettier is available
if ! command -v npx >/dev/null 2>&1; then
    exit 0
fi

# Run formatting with timeout
timeout $TIMEOUT npx prettier --write --cache --loglevel=silent "**/*.{ts,tsx,js,jsx,mdx}" 2>/dev/null || true

exit 0