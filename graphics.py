from tkinter import *
from tkinter import messagebox

from logic import *
from functools import partial
from threading import *
from time import *


class GameFrame(Frame):
    def __init__(self, root, gameid: int = None, onlinemode: list = None):
        self.logi = logi(onlinemode, gameid)
        self.root = root
        root.geometry("400x200")
        root.title("Fuck Zilas")
        Frame.__init__(self, root)
        self.goal = 3
        self.size = 3
        self.kColor = "cyan"
        self.bColor = "red"
        self.defaultcolor = "white"
        self.switchcolor = "green"
        self.switch = None
        self.onlinemode = onlinemode



        # These buttons show whose turn it is
        self.kLabel = Button(self.root, text="Kryds", bg=self.kColor)
        self.kLabel.grid(row=0, column=self.size + 1, sticky="NSEW")
        self.bLabel = Button(self.root, text="Bolle", bg=self.bColor)
        self.bLabel.grid(row=1, column=self.size + 1, sticky="NSEW")

        self._start()

        # Start mysql fetcher thread
        self.loop = Thread(target=self.mysqlLoop)
        if self.onlinemode is not None:
            self.loop.start()

    def _ButtonPress(self, x, y):
        try:
            if self.logi.getonlineMode()[0] == "kryds" and self.logi.getTurn() == 0:
                return
            if self.logi.getonlineMode()[0] == "bolle" and self.logi.getTurn() == 1:
                return
        except TypeError:
            pass

        # Convert x and y cordinates to a number to find the pressed button in a list with all buttons.
        num = x * self.size + y
        button = self.logi.getPos()[num]
        print(self.logi.getKryds())
        print(self.logi.getBolle())

        def _bChanges(player: str):
            # prevents changes to the opponents score
            if player == "kryds" and self.logi.getBolle().count(num) != 0:
                return
            if player == "bolle" and self.logi.getKryds().count(num) != 0:
                return

            # Move your score if it has been marked
            if self.switch is not None:
                # Prevents replacing your already placed scores
                if player == "kryds" and self.logi.getKryds().count(num) != 0:
                    return
                if player == "bolle" and self.logi.getBolle().count(num) != 0:
                    return
                # Add score to list and remove color from the removed score
                self.logi.SetScore(player, num, self.switch)
                self.logi.getPos()[self.switch]["background"] = self.defaultcolor
                self.switch = None
                # hide valid move spots
                for b in range(9):
                    but = self.logi.getPos()[b]
                    if but["background"] == self.switchcolor:
                        but["background"] = self.defaultcolor

            # Mark your own score for moving
            if self.logi.getKryds().count(num) != 0 or self.logi.getBolle().count(num) != 0:
                # Show valid move spots
                for b in range(9):
                    but = self.logi.getPos()[b]
                    if but["background"] == self.defaultcolor:
                        self.switch = num
                        but["background"] = self.switchcolor
                return True

            # Change button to corresponding color and flip the turn
            if player == "kryds":
                button.configure(bg=self.kColor)
            elif player == "bolle":
                button.configure(bg=self.bColor)
            self._turncolor()

            # Change score list and remove color from button that isn't scored anymore (The oldest score is replaced if
            # there's more than 3 scores for a player)
            score = self.logi.SetScore(player, num)
            if score is not None:
                lastB = self.logi.getPos()[score]
                lastB.configure(bg=self.defaultcolor)

            # Check if someone won
            whoWon = self.logi.CheckWin(player)
            if whoWon is not None:
                pass
            print(self.logi.getKryds())
            self.logi.onlinenext()

        # check whose turn it is.
        if self.logi.getTurn() == 1:
            _bChanges("kryds")
        elif self.logi.getTurn() == 0:
            _bChanges("bolle")
        else:
            print("Something broke N' yeeted")
        if self.onlinemode is not None:
            self.logi.nextTurn()

    def _turncolor(self):
        if self.onlinemode is not None:
            if self.logi.getTurn() == 1:
                self.kLabel.configure(bg=self.kColor)
                self.bLabel.configure(bg=self.defaultcolor)
            elif self.logi.getTurn() == 0:
                self.bLabel.configure(bg=self.bColor)
                self.kLabel.configure(bg=self.defaultcolor)
            return

        # Switch the color of the side labels
        if self.logi.getTurn() == 0:
            self.kLabel.configure(bg=self.kColor)
            self.bLabel.configure(bg=self.defaultcolor)
        elif self.logi.getTurn() == 1:
            self.bLabel.configure(bg=self.bColor)
            self.kLabel.configure(bg=self.defaultcolor)
        else:
            print("turncolor broke")
        # Switches a number indicating whose turn it is

        self.logi.nextTurn()

    # Buttons gets created with a x and y variable attached to its click function
    def _buttons(self, size):
        for x in range(size):
            for y in range(size):
                btn = Button(self.root, bg=self.defaultcolor, command=partial(self._ButtonPress, x, y))
                btn.grid(column=x, row=y, sticky="NSEW")
                btn.config(width=6, height=2)
                # Reference to button is appended in a list
                self.logi.StorePos(btn)

    def resetbuttcolors(self):
        for _ in range(self.size * self.size):
            butt = self.logi.getPos()[_]
            if _ in self.logi.getBolle():
                butt.configure(bg=self.bColor)
            if _ in self.logi.getKryds():
                butt.configure(bg=self.kColor)

    # Function for setup things
    def _start(self):
        # Make rows stretchable
        for x in range(self.size):
            self.root.columnconfigure(x, weight=2)
            self.root.rowconfigure(x, weight=2)
        self.root.columnconfigure(self.size + 1, weight=1)
        self._buttons(self.size)
        print("start first")
        self.resetbuttcolors()

        # Set the turn color
        self._turncolor()

    def test(self):
        self.root.destroy()

    def _manualturn(self):
        self.logi.nextTurn()

    def setdeadness(self):
        self.logi.setdeadness()

    def mysqlLoop(self):
        while True:
            if self.logi.getdeadness():
                break

            if self.logi.getmove() == self.logi.getonlinemove():
                self.logi.getonlineData()
                self._turncolor()
                self.resetbuttcolors()
                print("update")
            print("mysql")
            sleep(1)


class StartWindow:
    def __init__(self, root):
        self.root = root

        self.window = Toplevel(root)
        self.window.protocol("WM_DELETE_WINDOW", self.root.destroy)

        self.gameid = StringVar()
        self.gameid.set("GameID")
        self.kryds = Button(self.window, text="Kryds", command=self.kryds)
        self.kryds.grid(row=0, column=0, sticky="NSEW")
        self.bolle = Button(self.window, text="Bolle", command=self.bolle)
        self.bolle.grid(row=0, column=1, sticky="NSEW")
        self.entry = Entry(self.window, text=self.gameid, width=6)
        self.entry.grid(row=1, column=0, sticky="NSEW")
        self.offline = Button(self.window, text="offline", command=self.offline)
        self.offline.grid(row=1, column=1, sticky="NSEW")
        root.withdraw()

        self.GameFrame = None

        for x in range(2):
            self.window.columnconfigure(x, weight=1)
            self.window.rowconfigure(x, weight=1)

    def bolle(self):
        try:
            if int(self.gameid.get()) is not int:
                self.window.destroy()
                self.root.deiconify()
                self.GameFrame = GameFrame(self.root, self.gameid.get(), ["bolle"])
            else:
                messagebox.showwarning("Error 18", "This is not a valid GameID")
        except ValueError:
            messagebox.showwarning("Error 18", "This is not a valid GameID")
            return

    def kryds(self):
        try:
            if int(self.gameid.get()) is not int:
                self.window.destroy()
                self.root.deiconify()
                self.GameFrame = GameFrame(self.root, self.gameid.get(), ["kryds"])
            else:
                messagebox.showwarning("Error 18", "This is not a valid GameID")
        except ValueError:
            messagebox.showwarning("Error 18", "This is not a valid GameID")
            return

    def offline(self):
        self.window.destroy()
        self.root.deiconify()
        self.GameFrame = GameFrame(self.root)

    def setdeadness(self):
        if self.GameFrame is not None:
            self.GameFrame.setdeadness()
