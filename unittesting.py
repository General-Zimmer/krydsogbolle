import unittest
from tkinter import *
import logic as logic
import data as data
import graphics as gfx


class DataTests(unittest.TestCase):
    def setUp(self):
        self.data = data.data()

    def test_setscore(self):
        pass

    def tearDown(self):
        pass


class LogiTests(unittest.TestCase):
    def setUp(self):
        root = Tk()
        self.gfx = gfx.gui(root)

    def test_checkwin1(self):
        self.gfx.logi.SetScore("bolle", 0)
        self.gfx.logi.SetScore("bolle", 3)
        self.gfx.logi.SetScore("bolle", 6)

        self.assertEqual(self.gfx.logi.CheckWin("bolle"), "bolle")

    def test_checkwin2(self):
        self.gfx.logi.SetScore("bolle", 6)
        self.gfx.logi.SetScore("bolle", 7)
        self.gfx.logi.SetScore("bolle", 8)

        self.assertEqual(self.gfx.logi.CheckWin("bolle"), "bolle")

    def test_checkwin3(self):
        self.gfx.logi.SetScore("bolle", 6)
        self.gfx.logi.SetScore("bolle", 4)
        self.gfx.logi.SetScore("bolle", 2)

        self.assertEqual(self.gfx.logi.CheckWin("bolle"), "bolle")

    def test_checkwin4(self):
        self.gfx.logi.SetScore("bolle", 0)
        self.gfx.logi.SetScore("bolle", 4)
        self.gfx.logi.SetScore("bolle", 8)

        self.assertEqual(self.gfx.logi.CheckWin("bolle"), "bolle")

    def tearDown(self):
        pass
