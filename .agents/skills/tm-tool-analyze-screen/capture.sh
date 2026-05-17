#!/bin/bash
# Self-contained capture script for tm-tool-analyze-screen
# Saves to project-local tmp directory and returns the path

# Use git to find the project root reliably
PROJECT_ROOT=$(git rev-parse --show-toplevel 2>/dev/null)

# Fallback to relative path if git fails
if [ -z "$PROJECT_ROOT" ]; then
    SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
    PROJECT_ROOT="$(cd "$SCRIPT_DIR/../../.." && pwd)"
fi

OUTPUT_DIR="$PROJECT_ROOT/tmp"
mkdir -p "$OUTPUT_DIR"
OUTPUT_FILE="$OUTPUT_DIR/gemini_screenshot.png"

# Execute interactive capture (waits for user to draw rectangle)
gnome-screenshot -a -f "$OUTPUT_FILE"

# Return the absolute path to stdout so the agent can read it
echo "$OUTPUT_FILE"
