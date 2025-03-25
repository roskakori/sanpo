# Copyright (c) 2021, Thomas Aglassinger
# All rights reserved. Distributed under the BSD 3-Clause License.
from pathlib import Path
from typing import Optional
from unittest import TestCase

TEST_TEMP_FOLDER = Path(__file__).parent / "temp"


class PoFileTest(TestCase):
    def setUp(self):
        self._po_paths_to_remove = []

    def write_po_file(self, test_name: str):
        po_lines = [
            "# Some translations",
            'msgid ""',
            'msgstr ""',
            r'"Project-Id-Version: PACKAGE VERSION\n"',
            r'"Report-Msgid-Bugs-To: \n"',
            r'"POT-Creation-Date: 2021-01-01\\n"',
            r'"PO-Revision-Date: 2021-01-01\\n"',
            r'"Last-Translator: FULL NAME EMAIL@ADDRESS\n"',
            r'"Language-Team: LANGUAGE LL@li.org\n"',
            "",
            'msgid "spam"',
            'msgstr ""',
        ]
        self.po_path = TEST_TEMP_FOLDER / (test_name + ".po")
        self.po_path.write_text("\n".join(po_lines) + "\n")
        self._po_paths_to_remove.append(self.po_path)

    def po_lines(self, po_path: Optional[Path] = None) -> list[str]:
        actual_po_path = po_path if po_path is not None else self.po_path
        return actual_po_path.read_text().split("\n")

    def tearDown(self):
        for po_path_to_remove in self._po_paths_to_remove:
            po_path_to_remove.unlink()
