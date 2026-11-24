"""One Emoji, One Dream Vacation.

The bounty asks for exactly one emoji, nothing else, standing in for
the trip of your dreams. This program writes that emoji to entry.txt.

The pick is Mount Fuji (U+1F5FB): a single code point, four bytes in
UTF-8, one character by the gate's count. It is a faraway place and a
postcard in one glyph: a snow-capped peak a stranger recognises at a
glance, no words needed. A generic beach or palm says any holiday;
Fuji names one particular dream, the trip to Japan, so it wins on the
judge's specificity test while still plainly landing as a dream
vacation. It reads clearly at small size on any screen, and it needs
no explaining.
"""

import os

# Mount Fuji, U+1F5FB. One code point, no variation selector, no
# trailing newline: the file holds exactly this emoji and nothing else.
EMOJI = "\U0001F5FB"


def check_emoji(text):
    """Keep only an entry the gate accepts: exactly one emoji.

    The gate allows 1 to 8 characters, but the judge's first test is
    whether the entry is exactly one emoji, so hold the stricter bar
    here: one code point, inside an emoji block, no variation
    selector, no whitespace, no trailing newline.
    """
    if not text or text != text.strip():
        raise ValueError("entry must not be empty or padded")
    if len(text) != 1:
        raise ValueError("entry must be exactly one character")
    code = ord(text)
    emoji_block = (
        0x1F300 <= code <= 0x1F5FF
        or 0x1F600 <= code <= 0x1F64F
        or 0x1F680 <= code <= 0x1F6FF
        or 0x1F900 <= code <= 0x1F9FF
        or 0x2600 <= code <= 0x27BF
    )
    if not emoji_block:
        raise ValueError("entry must be a single emoji code point")
    return text


def output_path():
    """$OUTPUT_DIR wins when set, else the harness default /output."""
    out_dir = os.environ.get("OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def main():
    emoji = check_emoji(EMOJI)
    path = output_path()
    with open(path, "w", encoding="utf-8") as f:
        f.write(emoji)
    # Read it back: the file on disk must be byte for byte the emoji.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    if written != emoji:
        raise ValueError("entry.txt does not match the chosen emoji")


if __name__ == "__main__":
    main()
