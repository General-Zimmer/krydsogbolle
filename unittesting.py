import unittest
import logic as logic
import data as data


class DataTests(unittest.TestCase):
    def setUp(self):
        self.data = data.data

    def test_setscore(self):
        self.assertIsNone(self.data.Setscore())

    def tearDown(self):
        pass


class LogiTests(unittest.TestCase):
    def setUp(self):
        self.logi = logic.logi

    def test_checkwin(self):
        self.logi.CheckWin()

    def tearDown(self):
        pass
