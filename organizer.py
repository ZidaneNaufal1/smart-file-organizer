import argparse
import shutil
from pathlib import Path


CATEGORIES = {
    "Images": {
        ".jpg",
        ".jpeg",
        ".png",
        ".gif",
        ".bmp",
        ".svg",
        ".webp",
    },
    "Documents": {
        ".pdf",
        ".doc",
        ".docx",
        ".txt",
        ".md",
        ".csv",
        ".xls",
        ".xlsx",
        ".ppt",
        ".pptx",
    },
    "Videos": {
        ".mp4",
        ".mkv",
        ".avi",
        ".mov",
        ".wmv",
        ".webm",
    },
    "Audio": {
        ".mp3",
        ".wav",
        ".flac",
        ".aac",
        ".ogg",
        ".m4a",
    },
    "Archives": {
        ".zip",
        ".rar",
        ".7z",
        ".tar",
        ".gz",
    },
    "Code": {
        ".py",
        ".js",
        ".html",
        ".css",
        ".java",
        ".cpp",
        ".c",
        ".json",
        ".yml",
        ".yaml",
    },
}


def get_category(file_path):
    """Return the category name for a file."""

    extension = file_path.suffix.lower()

    for category, extensions in CATEGORIES.items():
        if extension in extensions:
            return category

    return "Others"


def get_unique_destination(destination):
    """Prevent an existing file from being overwritten."""

    if not destination.exists():
        return destination

    counter = 1

    while True:
        candidate = destination.with_name(
            f"{destination.stem}_{counter}{destination.suffix}"
        )

        if not candidate.exists():
            return candidate

        counter += 1


def collect_files(source, include_hidden=False):
    """Collect files located directly inside the source folder."""

    files = []

    for item in source.iterdir():
        if not item.is_file():
            continue

        if not include_hidden and item.name.startswith("."):
            continue

        files.append(item)

    return sorted(files, key=lambda path: path.name.lower())


def organize_directory(source, apply_changes=False, include_hidden=False):
    """Preview or apply file organization."""

    source = Path(source).expanduser().resolve()

    if not source.exists():
        raise ValueError(f"Folder tidak ditemukan: {source}")

    if not source.is_dir():
        raise ValueError(f"Lokasi bukan sebuah folder: {source}")

    files = collect_files(
        source,
        include_hidden=include_hidden,
    )

    plans = []

    for file_path in files:
        category = get_category(file_path)
        category_folder = source / category
        destination = category_folder / file_path.name
        destination = get_unique_destination(destination)

        plans.append((file_path, destination))

    if not plans:
        print("Tidak ada file yang perlu diorganisasi.")
        return 0

    mode = "APPLY" if apply_changes else "DRY RUN"

    print(f"\nMode: {mode}")
    print(f"Folder: {source}\n")

    moved_count = 0

    for file_path, destination in plans:
        relative_destination = destination.relative_to(source)

        print(
            f"{file_path.name} -> "
            f"{relative_destination}"
        )

        if apply_changes:
            destination.parent.mkdir(
                parents=True,
                exist_ok=True,
            )

            shutil.move(
                str(file_path),
                str(destination),
            )

            moved_count += 1

    if apply_changes:
        print(f"\nSelesai: {moved_count} file dipindahkan.")
    else:
        print(
            "\nPratinjau selesai. "
            "Tidak ada file yang dipindahkan."
        )
        print(
            "Tambahkan opsi --apply "
            "untuk menjalankan perubahan."
        )

    return moved_count


def build_parser():
    """Create the command-line argument parser."""

    parser = argparse.ArgumentParser(
        description=(
            "Organize files into category folders "
            "without overwriting existing files."
        )
    )

    parser.add_argument(
        "folder",
        nargs="?",
        default=".",
        help="Folder yang ingin diorganisasi.",
    )

    parser.add_argument(
        "--apply",
        action="store_true",
        help="Benar-benar memindahkan file.",
    )

    parser.add_argument(
        "--include-hidden",
        action="store_true",
        help="Sertakan file tersembunyi.",
    )

    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()

    try:
        organize_directory(
            args.folder,
            apply_changes=args.apply,
            include_hidden=args.include_hidden,
        )
    except ValueError as error:
        parser.error(str(error))


if __name__ == "__main__":
    main()
