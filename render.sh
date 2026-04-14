#!/usr/bin/env bash
#
# render.sh — batch-render every .html in a folder to a 1080x1350 PNG using
# headless Chrome. The output PNG sits next to the HTML with the same basename.
#
# Usage:
#   ./render.sh Outputs/agentes-claude-code           # render every .html in the folder
#   ./render.sh Outputs/agentes-claude-code/cover.html  # render a single file
#
# Requires:
#   - Google Chrome installed at /c/Program Files/Google/Chrome/Application/chrome.exe
#     (Windows default install path; override with CHROME=/path/to/chrome ./render.sh ...)
#

set -euo pipefail

CHROME="${CHROME:-/c/Program Files/Google/Chrome/Application/chrome.exe}"

if [ ! -f "$CHROME" ]; then
  echo "❌ Chrome not found at: $CHROME" >&2
  echo "   Override with: CHROME=/path/to/chrome ./render.sh ..." >&2
  exit 1
fi

if [ $# -eq 0 ]; then
  echo "Usage: $0 <folder-or-html-file>" >&2
  echo "Example: $0 Outputs/agentes-claude-code" >&2
  exit 1
fi

TARGET="$1"

render_one() {
  local html_file="$1"
  local abs
  abs="$(cd "$(dirname "$html_file")" && pwd)/$(basename "$html_file")"
  local png="${abs%.html}.png"
  local name
  name="$(basename "$html_file")"

  # Convert Git Bash path (/c/Visual_posts/...) to Windows path (c:/Visual_posts/...)
  # so that Chrome on Windows can resolve the file:// URL.
  local win_path="$abs"
  if [[ "$abs" =~ ^/([a-zA-Z])/(.*) ]]; then
    win_path="${BASH_REMATCH[1]}:/${BASH_REMATCH[2]}"
  fi

  local win_png="$png"
  if [[ "$png" =~ ^/([a-zA-Z])/(.*) ]]; then
    win_png="${BASH_REMATCH[1]}:/${BASH_REMATCH[2]}"
  fi

  # Render at a slightly larger viewport (1098x1368) to avoid Chrome's
  # black-border artifact on Windows, then crop to exact 1080x1350.
  "$CHROME" \
    --headless=new \
    --disable-gpu \
    --hide-scrollbars \
    --force-device-scale-factor=1 \
    --window-size=1098,1368 \
    --virtual-time-budget=5000 \
    --screenshot="$win_png" \
    "file:///$win_path" 2>/dev/null

  if [ -f "$png" ]; then
    # Crop to exact Instagram 4:5 dimensions (1080x1350)
    python -c "
from PIL import Image
img = Image.open('$win_png')
if img.size != (1080, 1350):
    cropped = img.crop((0, 0, 1080, 1350))
    cropped.save('$win_png')
" 2>/dev/null

    local size
    size="$(wc -c < "$png" | tr -d ' ')"
    printf "  ✅ %-40s → %s bytes\n" "$name" "$size"
  else
    printf "  ❌ %-40s (failed)\n" "$name"
    return 1
  fi
}

if [ -f "$TARGET" ]; then
  # Single file mode
  case "$TARGET" in
    *.html)
      echo "Rendering single file: $TARGET"
      render_one "$TARGET"
      ;;
    *)
      echo "❌ Not an .html file: $TARGET" >&2
      exit 1
      ;;
  esac
elif [ -d "$TARGET" ]; then
  # Folder mode
  echo "Rendering all .html in: $TARGET"
  count=0
  for f in "$TARGET"/*.html; do
    [ -e "$f" ] || { echo "  (no .html files found)"; exit 0; }
    render_one "$f"
    count=$((count + 1))
  done
  echo ""
  echo "Done. Rendered $count file(s)."
else
  echo "❌ Not a file or directory: $TARGET" >&2
  exit 1
fi
