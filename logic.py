from data import *


class logi:
    def __init__(self, onlinemode, gameid):
        self.data = data(onlinemode, gameid)

    def CheckWin(self, player: str):
        score = None
        # Get sorted list of the data to be checked
        if player == "kryds" and self.data.getKryds() is not None:
            score = sorted(self.data.getKryds())
        elif player == "bolle" and self.data.getBolle() is not None:
            score = sorted(self.data.getBolle())

        # You can't win if you don't have 3 scores
        if len(score) < 3:
            return None
        middle = score[1]
        # First check the middle score for vertical victories
        if middle in [1, 4, 7]:
            # Check if the first and last score is in the correct place
            if middle == (score[0] + 1) and middle == (score[2] - 1):
                print(player + " vandt")
                return player
        # Then check the middle score for horrizontel victories
        if middle in [3, 4, 5]:
            # Check if the first and last score is in the correct place
            if middle == (score[0] + 3) and middle == (score[2] - 3):
                print(player + " vandt")
                return player
        # Last check the middle score for diagonal victories
        if middle == 4:
            # Check if the first and last score is in the correct place
            if middle == (score[0] + 4) and middle == (score[2] - 4) or middle == (score[0] + 2) and middle == (
                    score[2] - 2):
                print(player + " vandt")
                return player

        return None

    # Do you need comments to getter and setter functions?
    def SetScore(self, player: str, num: int, button=None):
        return self.data.Setscore(player, num, button)

    def StorePos(self, content):
        self.data.addpos(content)

    def getPos(self):
        return self.data.getPos()

    def getBolle(self):
        return self.data.getBolle()

    def getKryds(self):
        return self.data.getKryds()

    def nextTurn(self):
        self.data.nextTurn()

    def getTurn(self):
        return self.data.turn

    def getonlineMode(self):
        return self.data.onlinemode

    def stoploop(self):
        pass

    def setdeadness(self):
        self.data.setdeadness()

    def setgameid(self, gid):
        self.data.setgameid(gid)

    def getdeadness(self):
        return self.data.deadprogram

    def onlinenext(self):
        self.data.onlinenext()

    def getonlineData(self):
        self.data.getonlineData()

    def getmove(self):
        return self.data.getmove()

    def getonlinemove(self):
        return self.data.getonlinemove()
