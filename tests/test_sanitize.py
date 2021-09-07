# Copyright (c) 2021, Thomas Aglassinger
# All rights reserved. Distributed under the BSD 3-Clause License.
from unittest import TestCase

from sanpo.sanitize import sanitize_file, sanitize_lines
from tests._common import PoFileTest


class SanitizationTest(TestCase):
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
        self.assertEqual(list(sanitize_lines(source_lines)), ["PRESERVE"])

    def test_can_preserve_metadata_lines(self):
        source_lines = [
            r'"Project-Id-Version: some 1.2.3\n"',
            r'"Report-Msgid-Bugs-To: bugs@example.com\n"',
            r'"Last-Translator: John Doe john@example.com\n"',
            r'"Language-Team: en en@example.com\n"',
        ]
        self.assertEqual(list(sanitize_lines(source_lines)), source_lines)


class TransformFileTest(PoFileTest):
    def test_can_remove_pointless_lines_in_file(self):
        self.write_po_file(self.test_can_remove_pointless_lines_in_file.__name__)
        initial_po_lines = self.po_lines()
        sanitize_file(self.po_path)
        transformed_po_lines = self.po_lines()
        self.assertNotEqual(initial_po_lines, transformed_po_lines)
