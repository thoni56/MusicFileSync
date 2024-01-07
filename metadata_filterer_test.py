import unittest
from unittest.mock import patch, MagicMock

from metadata_filterer import metadata_filter

class TestMetadataFiltererTest(unittest.TestCase):

    def setUp(self):
        self.patcher_for_tinytag_get = patch("metadata_filterer.tinytag.get")
        self.tinytag_get_mock = self.patcher_for_tinytag_get.start()
        self.tinytag_get_mock.return_value = MagicMock()
        pass

    def test_returns_no_files_if_no_files(self):
        self.assertEqual(metadata_filter([], {}), [])

    def test_returns_all_files_with_no_filter(self):
        self.assertEqual(metadata_filter(["a", "b", "c"], {}), ["a", "b", "c"])

    def test_return_only_files_with_matching_single_metadata(self):
        metadata_for_a = MagicMock()
        metadata_for_a.artist = ["a"]

        metadata_for_b = MagicMock()
        metadata_for_b.artist = ["b"]

        metadata_for_c = MagicMock()
        metadata_for_c.artist = ["c"]

        self.tinytag_get_mock.side_effect = [metadata_for_a, metadata_for_b, metadata_for_c]

        self.assertEqual(metadata_filter(["a", "b", "c"], {"artist": "a"}), ["a"])