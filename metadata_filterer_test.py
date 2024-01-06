import unittest
from unittest.mock import patch

from musicfilesync import sync

class TestMetadataFiltererTest(unittest.TestCase):

    def setUp(self):
        self.patcher_for_glob_glob = patch("metadata_filterer...")
        self.glob_glob_mock = self.patcher_for_glob_glob.start()
        self.glob_glob_mock.return_value = []
        pass

    def test_nothing_yet(self):
        pass