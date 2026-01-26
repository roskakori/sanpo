# Copyright (c) 2021, Thomas Aglassinger
# All rights reserved. Distributed under the BSD 3-Clause License.
from unittest.mock import patch

import pytest

from sanpo.command import main_without_logging_setup, po_paths_from

from ._common import TEST_TEMP_FOLDER, PoFileTest


class CommandTest(PoFileTest):
    def test_can_show_help(self):
        with self.assertRaises(SystemExit):
            main_without_logging_setup(["--help"])

    def test_can_show_version(self):
        with self.assertRaises(SystemExit):
            main_without_logging_setup(["--version"])

    def test_can_sanitize_single_file(self):
        self.write_po_file(self.test_can_sanitize_single_file.__name__)
        initial_po_lines = self.po_lines()
        assert main_without_logging_setup([self.po_path]) == 0
        sanitized_po_lines = self.po_lines()
        assert initial_po_lines != sanitized_po_lines

    def test_can_sanitize_multiple_files(self):
        po_path_to_sanitized_po_lines_map = {}
        file_count = 3
        for file_number in range(1, file_count + 1):
            test_name = f"{self.test_can_sanitize_multiple_files.__name__}_{file_number}"
            self.write_po_file(test_name)
            assert self.po_path not in po_path_to_sanitized_po_lines_map
            po_path_to_sanitized_po_lines_map[self.po_path] = self.po_lines()

        po_paths_to_sanitize = list(po_path_to_sanitized_po_lines_map.keys())
        assert main_without_logging_setup(po_paths_to_sanitize) == 0

        for po_path, initial_po_lines in po_path_to_sanitized_po_lines_map.items():
            sanitized_po_lines = self.po_lines(po_path)
            assert sanitized_po_lines != initial_po_lines

    def test_can_sanitize_none_arguments(self):
        self.write_po_file(self.test_can_sanitize_none_arguments.__name__)
        with patch("sys.argv", ["sanpo", str(self.po_path)]):
            assert main_without_logging_setup() == 0

    def test_can_skip_virtual_environments(self):
        self.write_po_file_with_name_parts(["valid.po"])
        self.write_po_file_with_name_parts(["some", "valid.po"])
        self.write_po_file_with_name_parts([".venv", "skip.po"])
        self.write_po_file_with_name_parts(["venv", "skip.po"])
        self.write_po_file_with_name_parts(["venv_kinky", "lib", "python3.14", "site-packages", "skip.po"])
        po_paths = list(po_paths_from([TEST_TEMP_FOLDER / "**" / "*.po"]))
        assert len(po_paths) == 2, f"po_path={po_paths}"
        for po_path in po_paths:
            assert po_path.name != "skip.po", f"po_path={po_path}"

    def test_can_process_folder_paths_without_po_pattern(self):
        self.write_po_file_with_name_parts(["some", "valid.po"])
        po_paths = list(po_paths_from([TEST_TEMP_FOLDER]))
        assert len(po_paths) == 1, f"po_path={po_paths}"
        assert po_paths[0].name == "valid.po"


def test_fails_on_non_existent_po_file():
    assert main_without_logging_setup(["no_such.po"]) == 1


def test_fails_on_no_po_files():
    with (
        pytest.raises(SystemExit) as error,
        patch("sys.argv", ["sanpo"]),
    ):
        main_without_logging_setup()
    assert error.value.code == 2
