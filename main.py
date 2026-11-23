"""One-line pitch entry for make.fun's "A Day of One-Line Pitches".

The program writes a single sentence to entry.txt in the grader's
output directory. The sentence is the whole entry: it has to convince
a friend who has never coded to let an AI agent build their first
app idea on make.fun, in one read.
"""

import os

PITCH = (
    "Describe your app idea in plain words and an AI agent on make.fun "
    "will build the first working version for you today — no coding, "
    "no jargon, and you stay in charge of every decision."
)


def main() -> None:
    text = PITCH.strip()
    if not 1 <= len(text) <= 240:
        raise SystemExit(f"pitch is {len(text)} chars, must be 1-240")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    try:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"wrote {path} ({len(text)} chars)")
    except OSError as exc:
        # The grader sets MAKEFUN_OUTPUT_DIR; if that directory is not
        # usable, fall back to the /output path the rules name.
        if os.path.abspath(out_dir) == "/output":
            raise SystemExit(f"cannot write entry.txt: {exc}")
        print(f"note: could not write {out_dir}: {exc}; trying /output")
        os.makedirs("/output", exist_ok=True)
        with open("/output/entry.txt", "w", encoding="utf-8") as f:
            f.write(text)
        print(f"wrote /output/entry.txt ({len(text)} chars)")
        return
    # The rules name /output/entry.txt as the scored file, so also leave
    # a copy there whenever it is a different directory and writable.
    if os.path.abspath(out_dir) != "/output":
        try:
            os.makedirs("/output", exist_ok=True)
            with open("/output/entry.txt", "w", encoding="utf-8") as f:
                f.write(text)
            print("also wrote /output/entry.txt")
        except OSError as exc:
            print(f"note: could not also write /output/entry.txt: {exc}")


if __name__ == "__main__":
    main()
