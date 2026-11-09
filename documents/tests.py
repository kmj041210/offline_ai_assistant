from django.test import SimpleTestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from .utils import extract_text


class DocumentExtractTest(SimpleTestCase):
    def test_txt_extraction(self):
        file = SimpleUploadedFile(
            "test.txt",
            "Hello Offline AI".encode("utf-8")
        )

        self.assertEqual(extract_text(file), "Hello Offline AI")