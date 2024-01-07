import unittest
from unittest.mock import patch

from musicfilesync import sync

class TestMusicFileSync(unittest.TestCase):

    def setUp(self):
        self.patcher_for_glob_glob = patch("musicfilesync.glob.glob")
        self.glob_glob_mock = self.patcher_for_glob_glob.start()
        self.glob_glob_mock.return_value = []
        self.patcher_for_filter_on_metadata = patch("musicfilesync.filter_on_metadata")
        self.filter_on_metadata_mock = self.patcher_for_filter_on_metadata.start()
        self.filter_on_metadata_mock.return_value = []
        self.patcher_for_update_files = patch("musicfilesync.update_files")
        self.update_files_mock = self.patcher_for_update_files.start()
        self.patcher_for_delete_nonexisting_files = patch("musicfilesync.delete_nonexisting_files")
        self.delete_nonexisting_files_mock = self.patcher_for_delete_nonexisting_files.start()
        self.delete_nonexisting_files_mock.return_value = []
        self.patcher_for_os_isfile = patch("musicfilesync.os.path.isfile")
        self.os_isfile_mock = self.patcher_for_os_isfile.start()
        self.os_isfile_mock.return_value = True

    def test_empty_source_and_destination_will_give_no_updates_or_deletes(self):
        self.update_files_mock.return_value = []
        
        self.assertEqual(sync("source_dir", "destination_dir"), ([], []))

        self.update_files_mock.assert_called_once_with("source_dir", [], "destination_dir")

    def test_one_file_in_source_will_give_that_as_updates(self):
        files = ["aFile.mp3"]
        self.glob_glob_mock.return_value = files
        self.filter_on_metadata_mock.return_value = files
        self.update_files_mock.return_value = files

        self.assertEqual(sync("source_dir", "destination_dir"), (files, []))

        self.update_files_mock.assert_called_once_with("source_dir", files, "destination_dir")

    def test_multiple_files_in_source_will_give_all_files_as_updates(self):
        files = ["file1.mp3", "file2.mp3", "file3.mp3"]
        self.glob_glob_mock.return_value = files
        self.filter_on_metadata_mock.return_value = files
        self.update_files_mock.return_value = files

        self.assertEqual(sync("source_dir", "destination_dir"), (files, []))

        self.update_files_mock.assert_called_once_with("source_dir", files, "destination_dir")

    def test_empty_source_and_destination_with_existing_files(self):
        self.update_files_mock.return_value = []
        self.delete_nonexisting_files_mock.return_value = ["file1.mp3", "file2.mp3", "file3.mp3"]

        self.assertEqual(sync("source_dir", "destination_dir"), ([], ["file1.mp3", "file2.mp3", "file3.mp3"]))

        self.update_files_mock.assert_called_once_with("source_dir", [], "destination_dir")


    def test_filters_should_be_propagated_to_filter_on_metadata(self):
        self.glob_glob_mock.return_value = ["file1.mp3", "file2.mp3"]
        self.filter_on_metadata_mock.return_value = ["file1.mp3", "file2.mp3"]
        self.update_files_mock.return_value = ["file1.mp3", "file2.mp3"]
        
        self.assertEqual(sync("source_dir", "destination_dir", {"genre":"rock"}), (["file1.mp3", "file2.mp3"], []))

        self.filter_on_metadata_mock.assert_called_once_with(["file1.mp3", "file2.mp3"], {"genre":"rock"})
        
    # More tests:
    # - filtering conditions to be propagated to source_

