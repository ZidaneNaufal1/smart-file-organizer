# Smart File Organizer

[![Tests](https://github.com/ZidaneNaufal1/smart-file-organizer/actions/workflows/tests.yml/badge.svg)](https://github.com/ZidaneNaufal1/smart-file-organizer/actions/workflows/tests.yml)
[![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-3776AB.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A safe Python command-line tool that organizes files into category
folders based on their extensions.

The application runs in dry-run mode by default, allowing users to
review every planned operation before any file is moved.

## Features

- Organizes files into category folders
- Safe dry-run mode by default
- Requires `--apply` before moving files
- Prevents existing files from being overwritten
- Handles file extensions without case sensitivity
- Ignores hidden files by default
- Supports optional hidden-file organization
- Uses only the Python standard library
- Includes automated tests

## Categories

| Category | Example Extensions |
|---|---|
| Images | `.jpg`, `.png`, `.gif`, `.svg`, `.webp` |
| Documents | `.pdf`, `.docx`, `.txt`, `.csv`, `.xlsx` |
| Videos | `.mp4`, `.mkv`, `.avi`, `.mov` |
| Audio | `.mp3`, `.wav`, `.flac`, `.m4a` |
| Archives | `.zip`, `.rar`, `.7z`, `.tar`, `.gz` |
| Code | `.py`, `.js`, `.html`, `.css`, `.json`, `.yml` |
| Others | Extensions not included above |

## Requirements

- Python 3.8 or newer
- No third-party packages

## Installation

Clone the repository:

```bash
git clone https://github.com/ZidaneNaufal1/smart-file-organizer.git
cd smart-file-organizer
```

## Usage

### Preview Changes

Dry-run mode is enabled by default:

```bash
python3 organizer.py /path/to/folder
```

The application displays where each file would be moved without
changing anything.

### Apply Changes

Use `--apply` to move the files:

```bash
python3 organizer.py /path/to/folder --apply
```

### Include Hidden Files

Hidden files are ignored by default. To include them:

```bash
python3 organizer.py /path/to/folder --include-hidden
```

To include hidden files and apply the changes:

```bash
python3 organizer.py /path/to/folder --include-hidden --apply
```

### Show Help

```bash
python3 organizer.py --help
```

## Example

Before:

```text
Downloads/
├── photo.jpg
├── report.pdf
├── song.mp3
└── project.zip
```

After running with `--apply`:

```text
Downloads/
├── Archives/
│   └── project.zip
├── Audio/
│   └── song.mp3
├── Documents/
│   └── report.pdf
└── Images/
    └── photo.jpg
```

## Safety

The application does not move files unless `--apply` is provided.

When a destination file already exists, the new file receives a
numbered name:

```text
report.pdf
report_1.pdf
report_2.pdf
```

Existing files are never overwritten.

For initial testing, use a temporary folder rather than an important
personal directory.

## Running the Tests

```bash
python3 -m unittest -v
```

The automated tests cover:

- Category detection
- Case-insensitive extensions
- Unknown extensions
- Dry-run safety
- Real file movement
- Filename collision handling
- Hidden-file behavior

## Reproducible Demo

Run the included demonstration:

```bash
python examples/run_demo.py
```

The script creates disposable sample files in a temporary directory, displays
the dry-run plan, applies it, and prints the resulting directory tree. It never
uses personal Downloads or Documents folders. The same demonstration runs in
GitHub Actions as a smoke test.

## Project Structure

```text
smart-file-organizer/
├── .github/
│   └── workflows/
│       └── tests.yml
├── organizer.py
├── test_organizer.py
├── examples/
│   └── run_demo.py
├── CONTRIBUTING.md
├── CHANGELOG.md
├── README.md
├── LICENSE
└── .gitignore
```

## Contributing

Contributions are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md) for the
local setup, safety rules, test commands, and pull request workflow.

## Releases

Release notes are maintained in [CHANGELOG.md](CHANGELOG.md). Stable versions
are published on the repository's
[Releases page](https://github.com/ZidaneNaufal1/smart-file-organizer/releases).

## Author

**Muhammad Zidane Naufal Azzam**

GitHub: [ZidaneNaufal1](https://github.com/ZidaneNaufal1)

## License

This project is available under the MIT License.
