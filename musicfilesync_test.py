from unittest.mock import patch

from musicfilesync import sync

@patch("musicfilesync.update")
@patch("musicfilesync.get_source_file_list")
def test_empty_source_and_destination_will_give_no_updates_or_deletes(get_source_file_list_mock, update_mock):
    update_mock.return_value = []
    assert sync("source", "destination") == ([], [])

@patch("musicfilesync.update")
@patch("musicfilesync.get_source_file_list")
def test_one_file_in_source_will_give_that_as_updates(get_source_file_list_mock, update_mock):
    update_mock.return_value = ["aFile.mp3"]
    assert sync("source", "destination") == (["aFile.mp3"], [])

# More tests:
# - filtering conditions to be propagated to source_file_lister
