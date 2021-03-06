import unittest
from tkinter import *
import logic as logic
from data import *
from graphics import *


class DataTests(unittest.TestCase):
    def setUp(self):
        self.data = data(None, None)

    def test_setscore(self):
        pass

    def tearDown(self):
        pass


class LogiTests(unittest.TestCase):
    def setUp(self):
        root = Tk()
        self.gfx = GameFrame(root)

    def test_checkwin1(self):
        self.gfx.logi.SetScore("bolle", 0)
        self.gfx.logi.SetScore("bolle", 3)
        self.gfx.logi.SetScore("bolle", 6)

        self.assertEqual("bolle", self.gfx.logi.CheckWin("bolle", "test"))

    def test_checkwin2(self):
        self.gfx.logi.SetScore("bolle", 6)
        self.gfx.logi.SetScore("bolle", 7)
        self.gfx.logi.SetScore("bolle", 8)

        self.assertEqual("bolle", self.gfx.logi.CheckWin("bolle", "test"))

    def test_checkwin3(self):
        self.gfx.logi.SetScore("bolle", 6)
        self.gfx.logi.SetScore("bolle", 4)
        self.gfx.logi.SetScore("bolle", 2)

        self.assertEqual("bolle", self.gfx.logi.CheckWin("bolle", "test"))

    def test_checkwin4(self):
        self.gfx.logi.SetScore("bolle", 0)
        self.gfx.logi.SetScore("bolle", 4)
        self.gfx.logi.SetScore("bolle", 8)

        self.assertEqual("bolle", self.gfx.logi.CheckWin("bolle", "test"))

    def test_checkwin5(self):
        self.gfx.logi.SetScore("bolle", 1)
        self.gfx.logi.SetScore("bolle", 2)
        self.gfx.logi.SetScore("bolle", 3)

        self.assertEqual(None, self.gfx.logi.CheckWin("bolle", "test"))

    def tearDown(self):
        pass


