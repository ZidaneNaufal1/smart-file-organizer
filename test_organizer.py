import io
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

from organizer import get_category, organize_directory


class FileOrganizerTests(unittest.TestCase):
    def setUp(self):
        self.temp_directory = tempfile.TemporaryDirectory()
        self.folder = Path(self.temp_directory.name)

    def tearDown(self):
        self.temp_directory.cleanup()

    def run_organizer(self, apply_changes=False):
        output = io.StringIO()

        with redirect_stdout(output):
            result = organize_directory(
                self.folder,
                apply_changes=apply_changes,
            )

        return result, output.getvalue()

    def test_get_category_is_case_insensitive(self):
        self.assertEqual(
            get_category(Path("photo.JPG")),
            "Images",
        )
        self.assertEqual(
            get_category(Path("report.PDF")),
            "Documents",
        )

    def test_unknown_extension_uses_others(self):
        self.assertEqual(
            get_category(Path("mystery.xyz")),
            "Others",
        )

    def test_dry_run_does_not_move_file(self):
        source_file = self.folder / "photo.jpg"
        source_file.write_text("image data")

        moved_count, output = self.run_organizer(
            apply_changes=False,
        )

        self.assertEqual(moved_count, 0)
        self.assertTrue(source_file.exists())
        self.assertFalse(
            (self.folder / "Images" / "photo.jpg").exists()
        )
        self.assertIn("DRY RUN", output)

    def test_apply_moves_file_to_category(self):
        source_file = self.folder / "report.pdf"
        source_file.write_text("document data")

        moved_count, output = self.run_organizer(
            apply_changes=True,
        )

        destination = (
            self.folder
            / "Documents"
            / "report.pdf"
        )

        self.assertEqual(moved_count, 1)
        self.assertFalse(source_file.exists())
        self.assertTrue(destination.exists())
        self.assertEqual(
            destination.read_text(),
            "document data",
        )
        self.assertIn("APPLY", output)

    def test_existing_file_is_not_overwritten(self):
        documents = self.folder / "Documents"
        documents.mkdir()

        existing_file = documents / "report.pdf"
        existing_file.write_text("old document")

        source_file = self.folder / "report.pdf"
        source_file.write_text("new document")

        self.run_organizer(apply_changes=True)

        renamed_file = documents / "report_1.pdf"

        self.assertEqual(
            existing_file.read_text(),
            "old document",
        )
        self.assertTrue(renamed_file.exists())
        self.assertEqual(
            renamed_file.read_text(),
            "new document",
        )

    def test_hidden_file_is_ignored_by_default(self):
        hidden_file = self.folder / ".secret.txt"
        hidden_file.write_text("secret")

        moved_count, output = self.run_organizer(
            apply_changes=True,
        )

        self.assertEqual(moved_count, 0)
        self.assertTrue(hidden_file.exists())
        self.assertIn(
            "Tidak ada file",
            output,
        )


if __name__ == "__main__":
    unittest.main()
