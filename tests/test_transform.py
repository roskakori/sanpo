import os
from unittest import TestCase

from sanpo.transform import transformed_lines

_TEST_TEMP_FOLDER = os.path.join(os.path.dirname(__file__), "temp")


class TransformTest(TestCase):
    def test_can_remove_pointless_lines(self):
        source_lines = [
            r'"Project-Id-Version: PACKAGE VERSION\n"',
            r'"Report-Msgid-Bugs-To: \n"',
            r'"POT-Creation-Date: 2021-01-01\\n"',
            r'"PO-Revision-Date: 2021-01-01\\n"',
            r'"Last-Translator: FULL NAME EMAIL@ADDRESS\n"',
            r'"Language-Team: LANGUAGE LL@li.org\n"',
            "PRESERVE",
        ]
        self.assertEqual(list(transformed_lines(source_lines)), ["PRESERVE"])

    def test_can_preserve_metadata_lines(self):
        source_lines = [
            r'"Project-Id-Version: some 1.2.3\n"',
            r'"Report-Msgid-Bugs-To: bugs@example.com\n"',
            r'"Last-Translator: John Doe john@example.com\n"',
            r'"Language-Team: en en@example.com\n"',
        ]
        self.assertEqual(list(transformed_lines(source_lines)), source_lines)


class TransformFileTest(TestCase):
    def _write_po_file(self, test_name: str):
        po_lines = []
        po_path = os.path.join(_TEST_TEMP_FOLDER, test_name + ".po")
        with open(po_path, "w", encoding="utf-8") as po_file:
            for po_line in po_lines:
                po_file.write(f"{po_line}\n")

    def test_can_remove_pointless_lines(self):
        pass  # TODO
