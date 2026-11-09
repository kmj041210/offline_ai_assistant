from pathlib import Path
from pypdf import PdfReader


def extract_text(file):
    extension = Path(file.name).suffix.lower()

    if extension == ".txt":
        return file.read().decode("utf-8")

    if extension == ".pdf":
        reader = PdfReader(file)
        return "\n".join(
            page.extract_text() or ""
            for page in reader.pages
        )

    raise ValueError("Unsupported file format")