from Mysql import *


class data(mysql_connector):
    def __init__(self, onlinemode, gameid):
        mysql_connector.__init__(self)
        self.pos = []
        self.turn = [1]
        self.boller = []
        self.krydser = []
        self.onlinemode = onlinemode
        self.move = [0]
        self.deadprogram = False
        self.gameid = gameid

        if self.onlinemode is not None:
            test = mysql_connector.testrow(self, self.gameid)
            print(test)
            print("maybe")
            if test == 1:
                game = mysql_connector.pull(self, gameid)
                print(game)
                self.krydser = game[1]
                self.boller = game[2]
                self.turn = game[3]
                self.move = game[4]
            else:
                print("no")
                mysql_connector.add(self, self.gameid, "None", "None", self.turn[0], "0")

    def Setscore(self, player: str, num: int, button):
        result = None
        if player == "bolle":
            # check if a score is being replaced, then remove it
            if button is not None:
                self.boller.remove(button)
                return
            # Add score to list
            self.boller.append(num)
            # remove oldest if there's 4 or more scores in the list
            if len(self.boller) >= 4:
                result = self.boller[0]
                self.boller.pop(0)
        elif player == "kryds":
            # check if a button is being replaced, then remove it
            if button is not None:
                self.krydser.remove(button)
                return
            # Add score to list
            self.krydser.append(num)
            # remove oldest if there's 4 or more scores in the list
            if len(self.krydser) >= 4:
                result = self.krydser[0]
                self.krydser.pop(0)
        return result

    # Switches a number indicating whose turn it is
    def nextTurn(self):
        if self.turn[0] == 1:
            self.turn[0] = 0
        elif self.turn[0] == 0:
            self.turn[0] = 1

    # Well, yea. The rest probably don't need commenting
    def addpos(self, content):
        self.pos.append(content)

    def getPos(self):
        return self.pos

    def getTurn(self):
        return self.turn[0]

    def getBolle(self):
        return self.boller

    def getKryds(self):
        return self.krydser

    def getonlineMode(self):
        return self.onlinemode

    def getdeadness(self):
        return self.deadprogram

    def setdeadness(self):
        self.deadprogram = True

    def setgameid(self, gid):
        self.gameid = gid