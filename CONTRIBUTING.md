# Contributing

Thank you for helping improve Smart File Organizer.

## Before You Start

For a bug or larger feature, open an issue first so the expected behavior and
scope can be discussed before implementation.

Please keep these safety rules intact:

- Dry-run remains the default behavior.
- Files are moved only when `--apply` is provided.
- Existing files are never overwritten.
- Tests must not read, modify, or delete personal files.

## Local Setup

The project requires Python 3.8 or newer and has no third-party runtime
dependencies.

```bash
git clone https://github.com/ZidaneNaufal1/smart-file-organizer.git
cd smart-file-organizer
python3 -m unittest discover -v
```

## Making a Change

1. Create a branch from `main`.
2. Keep the change focused on one problem.
3. Add or update tests for behavior that changed.
4. Run the full test suite.
5. Update the README or changelog when users will notice the change.
6. Open a pull request explaining the problem, the solution, and how it was
   tested.

## Test Safety

Use temporary directories for filesystem tests. Never point automated tests at
a real Downloads, Documents, home, or project directory.

Run the checks used by continuous integration:

```bash
python3 -m py_compile organizer.py
python3 -m unittest discover -v
```

## Reporting a Bug

Include the operating system, Python version, command used, expected behavior,
actual behavior, and a minimal example that contains no private files or
credentials.

