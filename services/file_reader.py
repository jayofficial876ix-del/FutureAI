import os

from pypdf import PdfReader
from docx import Document


def read_file(filename):

    extension = os.path.splitext(filename)[1].lower()

    if extension == ".txt":

        with open(filename, "r", encoding="utf-8") as file:
            return file.read()

    elif extension == ".py":

        with open(filename, "r", encoding="utf-8") as file:
            return file.read()

    elif extension == ".html":

        with open(filename, "r", encoding="utf-8") as file:
            return file.read()

    elif extension == ".css":

        with open(filename, "r", encoding="utf-8") as file:
            return file.read()

    elif extension == ".js":

        with open(filename, "r", encoding="utf-8") as file:
            return file.read()

    elif extension == ".pdf":

        reader = PdfReader(filename)

        text = ""

        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

        return text

    elif extension == ".docx":

        doc = Document(filename)

        text = ""

        for paragraph in doc.paragraphs:
            text += paragraph.text + "\n"

        return text

    return None
