# Copyright (c) 2021, Thomas Aglassinger
# All rights reserved. Distributed under the BSD 3-Clause License.
import pytest

from sanpo.sanitize import sanitize_file, sanitized_lines
from tests._common import PoFileTest


def test_can_remove_pointless_lines():
    source_lines = [
        r'"Project-Id-Version: PACKAGE VERSION\n"',
        r'"Report-Msgid-Bugs-To: \n"',
        r'"POT-Creation-Date: 2021-01-01\\n"',
        r'"PO-Revision-Date: 2021-01-01\\n"',
        r'"Last-Translator: FULL NAME EMAIL@ADDRESS\n"',
        r'"Language-Team: LANGUAGE LL@li.org\n"',
        "PRESERVE",
    ]
    assert list(sanitized_lines(source_lines)) == ["PRESERVE"]


def test_can_preserve_metadata_lines():
    source_lines = [
        r'"Project-Id-Version: some 1.2.3\n"',
        r'"Report-Msgid-Bugs-To: bugs@example.com\n"',
        r'"Last-Translator: John Doe john@example.com\n"',
        r'"Language-Team: en en@example.com\n"',
    ]
    assert list(sanitized_lines(source_lines)) == source_lines


class TransformFileTest(PoFileTest):
    def test_can_remove_pointless_lines_in_file(self):
        self.write_po_file(self.test_can_remove_pointless_lines_in_file.__name__)
        initial_po_lines = self.po_lines()
        sanitize_file(self.po_path)
        transformed_po_lines = self.po_lines()
        assert initial_po_lines != transformed_po_lines

    def test_can_sanitize_str_path(self):
        self.write_po_file(self.test_can_sanitize_str_path.__name__)
        initial_po_lines = self.po_lines()
        sanitize_file(str(self.po_path))
        transformed_po_lines = self.po_lines()
        assert initial_po_lines != transformed_po_lines


def test_fails_on_int_po_file():
    with pytest.raises(TypeError, match="po_path must be a Path or str, but is <class 'int'>: 123"):
        sanitize_file(123)
