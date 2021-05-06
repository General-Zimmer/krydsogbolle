from tkinter import *
import logic as logik
from functools import partial


class gui(Frame):
    def __init__(self, root):
        self.logi = logik.logi()
        self.root = root
        root.geometry("400x200")
        Frame.__init__(self, root)
        self.grid(sticky="NSEW")
        self.goal = 3
        self.size = 3
        self.kColor = "cyan"
        self.bColor = "red"
        self.defaultcolor = "white"
        self.switchcolor = "green"
        self.switch = None
        self.kLabel = Button(self.root, text="Kryds", bg=self.kColor)
        self.kLabel.grid(row=0, column=self.size + 1, sticky="NSEW")
        self.bLabel = Button(self.root, text="Bolle", bg=self.bColor)
        self.bLabel.grid(row=1, column=self.size + 1, sticky="NSEW")
        self.start()

    def __ButtonPress__(self, x, y):

        num = x * self.size + y
        button = self.logi.getPos()[num]

        def __bChanges__(player: str):
            if player == "kryds" and self.logi.getBolle().count(num) != 0:
                return
            if player == "bolle" and self.logi.getKryds().count(num) != 0:
                return

            if self.switch is not None:
                if player == "kryds" and self.logi.getKryds().count(num) != 0:
                    return
                if player == "bolle" and self.logi.getBolle().count(num) != 0:
                    return
                self.logi.SetScore(player, num, self.switch)
                self.logi.getPos()[self.switch]["background"] = self.defaultcolor
                self.switch = None
                for b in range(9):
                    but = self.logi.getPos()[b]
                    if but["background"] == self.switchcolor:
                        but["background"] = self.defaultcolor

            if self.logi.getKryds().count(num) != 0 or self.logi.getBolle().count(num) != 0:
                for b in range(9):
                    but = self.logi.getPos()[b]
                    if but["background"] == self.defaultcolor:
                        self.switch = num
                        but["background"] = self.switchcolor
                return True

            if player == "kryds":
                button.configure(bg=self.kColor)
            elif player == "bolle":
                button.configure(bg=self.bColor)
            self.__turncolor__()
            score = self.logi.SetScore(player, num)
            if score is not None:
                lastB = self.logi.getPos()[score]
                lastB.configure(bg=self.defaultcolor)

            if self.logi.CheckWin(player) is not None:
                pass

        if self.logi.GetTurn() == 1:
            __bChanges__("kryds")
        elif self.logi.GetTurn() == 0:
            __bChanges__("bolle")
        else:
            print("Something broke N' yeeted")

    def __turncolor__(self):
        if self.logi.GetTurn() == 0:
            self.kLabel.configure(bg=self.kColor)
            self.bLabel.configure(bg=self.defaultcolor)
        else:
            self.bLabel.configure(bg=self.bColor)
            self.kLabel.configure(bg=self.defaultcolor)
        self.logi.NextTurn()

    def __buttons__(self, size):
        for x in range(size):
            for y in range(size):
                btn = Button(self.root, bg=self.defaultcolor, command=partial(self.__ButtonPress__, x, y))
                btn.grid(column=x, row=y, sticky="NSEW")
                btn.config(width=6, height=2)
                self.logi.StorePos(btn)

    def start(self):
        for x in range(self.size):
            self.root.columnconfigure(x, weight=2)
            self.root.rowconfigure(x, weight=2)
        self.root.columnconfigure(self.size+1, weight=1)
        self.__buttons__(self.size)
        self.__turncolor__()