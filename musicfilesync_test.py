import unittest
from unittest.mock import patch

from musicfilesync import sync

class TestMusicFileSync(unittest.TestCase):

    def setUp(self):
        self.patcher_for_get_source_file_list = patch("musicfilesync.get_source_file_list")
        self.get_source_file_list_mock = self.patcher_for_get_source_file_list.start()
        self.get_source_file_list_mock.return_value = []
        self.patcher_for_update_files = patch("musicfilesync.update_files")
        self.update_files_mock = self.patcher_for_update_files.start()
        self.patcher_for_delete_nonexisting_files = patch("musicfilesync.delete_nonexisting_files")
        self.delete_nonexisting_files_mock = self.patcher_for_delete_nonexisting_files.start()
        self.delete_nonexisting_files_mock.return_value = []

    def test_empty_source_and_destination_will_give_no_updates_or_deletes(self):
        self.update_files_mock.return_value = []
        
        self.assertEqual(sync("source_dir", "destination_dir"), ([], []))

        self.update_files_mock.assert_called_once_with("destination_dir", [])

    def test_one_file_in_source_will_give_that_as_updates(self):
        self.get_source_file_list_mock.return_value = ["aFile.mp3"]
        self.update_files_mock.return_value = ["aFile.mp3"]

        self.assertEqual(sync("source_dir", "destination_dir"), (["aFile.mp3"], []))

        self.update_files_mock.assert_called_once_with("destination_dir", ["aFile.mp3"])

    def test_multiple_files_in_source_will_give_all_files_as_updates(self):
        self.get_source_file_list_mock.return_value = ["file1.mp3", "file2.mp3", "file3.mp3"]
        self.update_files_mock.return_value = ["file1.mp3", "file2.mp3", "file3.mp3"]

        self.assertEqual(sync("source_dir", "destination_dir"), (["file1.mp3", "file2.mp3", "file3.mp3"], []))

        self.update_files_mock.assert_called_once_with("destination_dir", ["file1.mp3", "file2.mp3", "file3.mp3"])

    def test_empty_source_and_destination_with_existing_files(self):
        self.update_files_mock.return_value = []
        self.delete_nonexisting_files_mock.return_value = ["file1.mp3", "file2.mp3", "file3.mp3"]

        self.assertEqual(sync("source_dir", "destination_dir"), ([], ["file1.mp3", "file2.mp3", "file3.mp3"]))

        self.update_files_mock.assert_called_once_with("destination_dir", [])


    def test_filters_should_be_propagated_to_get_source_file_list(self):
        self.get_source_file_list_mock.return_value = ["file1.mp3", "file2.mp3"]
        self.update_files_mock.return_value = ["file1.mp3", "file2.mp3"]
        
        self.assertEqual(sync("source_dir", "destination_dir", {"genre":"rock"}), (["file1.mp3", "file2.mp3"], []))

        self.get_source_file_list_mock.assert_called_once_with("source_dir", {"genre":"rock"})
        
    # More tests:
    # - filtering conditions to be propagated to source_file_liste
