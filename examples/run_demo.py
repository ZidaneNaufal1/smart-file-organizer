#!/usr/bin/env python3
"""Run a safe, reproducible Smart File Organizer demonstration."""

from pathlib import Path
import sys
import tempfile


PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from organizer import organize_directory  # noqa: E402


def print_tree(root):
    for path in sorted(root.rglob("*"), key=lambda item: item.as_posix().lower()):
        if path.is_file():
            print(f"  {path.relative_to(root).as_posix()}")


def main():
    with tempfile.TemporaryDirectory(prefix="smart-organizer-demo-") as temporary:
        demo = Path(temporary)
        samples = {
            "holiday.JPG": "sample image",
            "report.pdf": "sample document",
            "theme.mp3": "sample audio",
            "notes.xyz": "unknown extension",
        }
        for name, content in samples.items():
            (demo / name).write_text(content, encoding="utf-8")

        print("BEFORE")
        print_tree(demo)

        print("\nDRY RUN")
        organize_directory(demo)
        assert all((demo / name).exists() for name in samples)

        print("\nAPPLY")
        moved = organize_directory(demo, apply_changes=True)
        assert moved == len(samples)

        print("\nAFTER")
        print_tree(demo)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
