import unittest
from tkinter import *
import logic as logic
import data as data
import graphics as gfx

class DataTests(unittest.TestCase):
    def setUp(self):
        self.data = data.data()

    def test_setscore(self):
        self.assertIsNone(self.data.Setscore())

    def tearDown(self):
        pass


class LogiTests(unittest.TestCase):
    def setUp(self):
        root = Tk()
        self.gfx = gfx.gui(root)


    def test_checkwin1(self):
        self.gfx.logi.SetScore("player", )
        self.gfx.logi.CheckWin("player")

    def tearDown(self):
        pass
