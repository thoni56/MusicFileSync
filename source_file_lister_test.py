import unittest
from unittest.mock import patch

from source_file_lister import get_source_file_list

class TestSourceFileLister(unittest.TestCase):

    def setUp(self):
        self.patcher_for_glob_glob = patch("source_file_lister.glob.glob")  
        self.glob_glob_mock = self.patcher_for_glob_glob.start()
        self.glob_glob_mock.return_value = []
        pass

    def test_will_return_empty_list_if_no_files_are_found(self):
        self.assertEqual(get_source_file_list("source_dir"), [])

    def test_will_return_list_of_one_file_if_one_music_file_is_found(self):
        self.glob_glob_mock.return_value = ["source_dir/file1.mp3"]
        self.assertEqual(get_source_file_list("source_dir", [".mp3"]), ["source_dir/file1.mp3"])

    def test_will_return_list_of_one_file_if_only_one_file_is_a_music_file(self):
        # This filtering is handled by glob so this test is for documentation.
        self.glob_glob_mock.return_value = ["source_dir/file1.mp3"]
        self.assertEqual(get_source_file_list("source_dir", [".mp3"]), ["source_dir/file1.mp3"])

    def test_will_return_list_of_two_files_even_if_they_have_different_music_file_extensions(self):
        # This filtering is handled by glob so this test is for documentation.
        self.glob_glob_mock.side_effect = [["source_dir/file1.mp3"], ["source_dir/file2.wav"]]
        self.assertEqual(get_source_file_list("source_dir", [".mp3", ".wav"]), ["source_dir/file1.mp3", "source_dir/file2.wav"])