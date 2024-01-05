import unittest
from unittest.mock import patch

from musicfilesync import sync

class TestMusicFileSync(unittest.TestCase):

    def setUp(self):
        self.patcher_for_get_source_file_list = patch("musicfilesync.get_source_file_list")
        self.get_source_file_list_mock = self.patcher_for_get_source_file_list.start()
        self.patcher_for_update = patch("musicfilesync.update")
        self.update_mock = self.patcher_for_update.start()

    def test_empty_source_and_destination_will_give_no_updates_or_deletes(self):
        self.update_mock.return_value = []
        assert sync("source", "destination") == ([], [])

    def test_one_file_in_source_will_give_that_as_updates(self):
        self.update_mock.return_value = ["aFile.mp3"]
        assert sync("source", "destination") == (["aFile.mp3"], [])

    # More tests:
    # - filtering conditions to be propagated to source_file_lister
    #
