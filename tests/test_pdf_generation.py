import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from scripts import build_resume


class PDFGenerationTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        root = Path(self.temporary.name)
        self.pdf = root / "resume.pdf"
        self.docx = root / "resume.docx"
        self.pdf.write_bytes(b"%PDF-stale")
        for name, value in (("PDF_PATH", self.pdf), ("DOCX_PATH", self.docx)):
            patcher = patch.object(build_resume, name, value)
            patcher.start()
            self.addCleanup(patcher.stop)

    def test_required_pdf_fails_without_libreoffice_and_removes_stale_output(self):
        with patch.object(build_resume, "find_libreoffice", return_value=None):
            with self.assertRaisesRegex(SystemExit, "LibreOffice not found"):
                build_resume.build_pdf(require_pdf=True)
        self.assertFalse(self.pdf.exists())

    def test_optional_pdf_can_be_skipped(self):
        with patch.object(build_resume, "find_libreoffice", return_value=None):
            build_resume.build_pdf()
        self.assertFalse(self.pdf.exists())

    def test_conversion_failure_does_not_leave_stale_output(self):
        failure = subprocess.CalledProcessError(1, "soffice", stderr="Conversion error")
        with patch.object(build_resume, "find_libreoffice", return_value="soffice"):
            with patch.object(build_resume.subprocess, "run", side_effect=failure):
                with self.assertRaisesRegex(SystemExit, "Conversion error"):
                    build_resume.build_pdf(require_pdf=True)
        self.assertFalse(self.pdf.exists())

    def test_successful_exit_without_pdf_is_rejected(self):
        result = subprocess.CompletedProcess([], 0, stdout="", stderr="")
        with patch.object(build_resume, "find_libreoffice", return_value="soffice"):
            with patch.object(build_resume.subprocess, "run", return_value=result):
                with self.assertRaisesRegex(SystemExit, "produced no PDF"):
                    build_resume.build_pdf(require_pdf=True)
        self.assertFalse(self.pdf.exists())

    def test_only_fresh_pdf_is_published(self):
        def convert(command, **kwargs):
            directory = Path(command[command.index("--outdir") + 1])
            (directory / "resume.pdf").write_bytes(b"%PDF-1.7\nfresh")
            return subprocess.CompletedProcess(command, 0, stdout="", stderr="")

        with patch.object(build_resume, "find_libreoffice", return_value="soffice"):
            with patch.object(build_resume.subprocess, "run", side_effect=convert):
                build_resume.build_pdf(require_pdf=True)
        self.assertEqual(self.pdf.read_bytes(), b"%PDF-1.7\nfresh")


if __name__ == "__main__":
    unittest.main()
