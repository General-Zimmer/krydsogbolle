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
        # Convert x and y cordinates to a number to find the pressed button in a list with all buttons.
        num = x * self.size + y
        button = self.logi.getPos()[num]

        def __bChanges__(player: str):
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

            # Change button to corresponding color
            if player == "kryds":
                button.configure(bg=self.kColor)
            elif player == "bolle":
                button.configure(bg=self.bColor)
            self.__turncolor__()

            # Change score list and remove color from button that isn't score anymore (The oldest score is replaced if
            # there's more than 3 scores for a player)
            score = self.logi.SetScore(player, num)
            if score is not None:
                lastB = self.logi.getPos()[score]
                lastB.configure(bg=self.defaultcolor)

            # Check if someone won
            whoWon = self.logi.CheckWin(player)
            if whoWon is not None:
                pass

        # check whose turn it is.
        if self.logi.GetTurn() == 1:
            __bChanges__("kryds")
        elif self.logi.GetTurn() == 0:
            __bChanges__("bolle")
        else:
            print("Something broke N' yeeted")

    def __turncolor__(self):
        # Switch the color of the side labels
        if self.logi.GetTurn() == 0:
            self.kLabel.configure(bg=self.kColor)
            self.bLabel.configure(bg=self.defaultcolor)
        elif self.logi.GetTurn() == 1:
            self.bLabel.configure(bg=self.bColor)
            self.kLabel.configure(bg=self.defaultcolor)
        else:
            print("turncolor broke")
        # Switches a number indicating if whose turn it is
        self.logi.NextTurn()

    # Buttons gets created with a x and y variable attached to its click function
    def __buttons__(self, size):
        for x in range(size):
            for y in range(size):
                btn = Button(self.root, bg=self.defaultcolor, command=partial(self.__ButtonPress__, x, y))
                btn.grid(column=x, row=y, sticky="NSEW")
                btn.config(width=6, height=2)
                # Button is appended in a list
                self.logi.StorePos(btn)

    # Function to start all necessary functions
    def start(self):
        for x in range(self.size):
            self.root.columnconfigure(x, weight=2)
            self.root.rowconfigure(x, weight=2)
        self.root.columnconfigure(self.size+1, weight=1)
        self.__buttons__(self.size)
        self.__turncolor__()
