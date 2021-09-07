# Copyright (c) 2021, Thomas Aglassinger
# All rights reserved. Distributed under the BSD 3-Clause License.
import os
from typing import List, Optional
from unittest import TestCase

TEST_TEMP_FOLDER = os.path.join(os.path.dirname(__file__), "temp")


class PoFileTest(TestCase):
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
        self.po_path = os.path.join(TEST_TEMP_FOLDER, test_name + ".po")
        with open(self.po_path, "w", encoding="utf-8") as po_file:
            for po_line in po_lines:
                po_file.write(f"{po_line}\n")

    def po_lines(self, po_path: Optional[str] = None) -> List[str]:
        actual_po_path = po_path if po_path is not None else self.po_path
        with open(actual_po_path, encoding="utf-8") as po_file:
            return list(line.rstrip("\n") for line in po_file)
