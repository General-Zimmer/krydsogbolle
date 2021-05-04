from tkinter import *
import logic as logik
from functools import partial


class gui(Frame):
    def __init__(self, root):
        self.logi = logik.logi()
        Frame.__init__(self, root)
        self.grid(sticky=W + S + N + E)
        self.goal = 3
        self.size = 3
        self.kColor = "cyan"
        self.bColor = "red"
        self.defaultcolor = "white"
        self.switchcolor = "green"
        self.switch = None
        self.kLabel = Button(self, text="Kryds", bg=self.kColor)
        self.kLabel.grid(row=0, column=self.size + 1, sticky=W + S + N + E)
        self.bLabel = Button(self, text="Bolle", bg=self.bColor)
        self.bLabel.grid(row=1, column=self.size + 1, sticky=W + S + N + E)

    def ButtonPress(self, x, y):

        if x == 0:
            num = y
        else:
            num = x * self.size + y
        button = self.logi.data.pos[num]

        def bChanges(player: str):
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
                self.logi.data.pos[self.switch]["background"] = self.defaultcolor
                self.switch = None
                for b in range(9):
                    but = self.logi.data.pos[b]
                    if but["background"] == self.switchcolor:
                        but["background"] = self.defaultcolor

            if self.logi.getKryds().count(num) != 0 or self.logi.getBolle().count(num) != 0:
                for b in range(9):
                    but = self.logi.data.pos[b]
                    if but["background"] == self.defaultcolor:
                        self.switch = num
                        but["background"] = self.switchcolor
                return True

            if player == "kryds":
                button.configure(bg=self.kColor)
            elif player == "bolle":
                button.configure(bg=self.bColor)
            self.turncolor()
            score = self.logi.SetScore(player, num)
            if score is not None:
                lastB = self.logi.data.pos[score]
                lastB.configure(bg=self.defaultcolor)

            if self.logi.CheckWin(player) is not None:
                pass

        if self.logi.GetTurn() == 1:
            bChanges("kryds")
        elif self.logi.GetTurn() == 0:
            bChanges("bolle")
        else:
            print("Something broke")

    def turncolor(self):
        if self.logi.GetTurn() == 0:
            self.kLabel.configure(bg=self.kColor)
            self.bLabel.configure(bg=self.defaultcolor)
        else:
            self.bLabel.configure(bg=self.bColor)
            self.kLabel.configure(bg=self.defaultcolor)
        self.logi.NextTurn()

    def buttons(self, size):
        for x in range(size):
            for y in range(size):
                btn = Button(self, bg=self.defaultcolor, command=partial(self.ButtonPress, x, y))
                btn.grid(column=x, row=y, sticky=N + S + E + W)
                btn.config(width=6, height=2)
                self.logi.StorePos(btn)

    def start(self):
        self.buttons(self.size)
        self.turncolor()
