import unittest
import logic as logic
import data as data


class DataTests(unittest.TestCase):
    def setUp(self):
        self.data = data.data()

    def test_setscore(self):
        self.assertIsNone(self.data.Setscore())

    def tearDown(self):
        pass


class LogiTests(unittest.TestCase):
    def setUp(self):
        self.logi = logic.logi()


    def test_checkwin1(self):
        for x in range(18):
            self.logi.StorePos(x)
        self.logi.CheckWin("player")

    def tearDown(self):
        pass
