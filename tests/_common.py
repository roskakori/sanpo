# Copyright (c) 2021, Thomas Aglassinger
# All rights reserved. Distributed under the BSD 3-Clause License.
from pathlib import Path
from unittest import TestCase

TEST_TEMP_FOLDER = Path(__file__).parent / "temp"

_PO_LINES = (
    "\n".join(
        [
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
    )
    + "\n"
)


class PoFileTest(TestCase):
    def setUp(self):
        self._po_paths_to_remove = []

    def write_po_file_with_name_parts(self, parts: list[str]) -> Path:
        actual_parts = parts if bool(parts) and parts[-1].endswith(".po") else [*parts, "test.po"]
        result = TEST_TEMP_FOLDER.joinpath(*actual_parts)
        result.parent.mkdir(parents=True, exist_ok=True)
        result.write_text(_PO_LINES)
        self._po_paths_to_remove.append(result)
        return result

    def write_po_file(self, test_name: str):
        self.po_path = TEST_TEMP_FOLDER / (test_name + ".po")
        self.po_path.write_text(_PO_LINES)
        self._po_paths_to_remove.append(self.po_path)

    def po_lines(self, po_path: Path | None = None) -> list[str]:
        actual_po_path = po_path if po_path is not None else self.po_path
        return actual_po_path.read_text().split("\n")

    def tearDown(self):
        for po_path_to_remove in self._po_paths_to_remove:
            po_path_to_remove.unlink()
