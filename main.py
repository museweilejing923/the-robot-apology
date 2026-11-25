"""Write the entry text to /output/entry.txt. Deterministic: no network, no randomness, no clock."""
import os
import sys
# The entry text: a robot apologising for one specific mistake, and what it learned.
ENTRY_TEXT = "I'm sorry I watered the plastic plant every morning for three weeks.\nI've learned to check whether something is alive before caring for it, so from now on I'll poke it first."
MAX_ENTRY_CHARS = 400


def _fail(msg):
    print("error: " + msg, file=sys.stderr)
    raise SystemExit(1)


def validate(t):
    if not t.strip():
        _fail("entry text must not be blank")
    if not any(c.isalpha() for c in t):
        _fail("entry text must contain at least one letter")
    if t.strip().isdigit():
        _fail("entry text must not be only digits")
    if len(t) > MAX_ENTRY_CHARS:
        _fail(f"entry text is {len(t)} characters, over the {MAX_ENTRY_CHARS} character limit")
    try:
        t.encode("utf-8")
    except UnicodeEncodeError as e:
        _fail(f"entry text is not valid UTF-8: {e}")


def main():
    validate(ENTRY_TEXT)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
