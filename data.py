class data:
    def __init__(self):
        self.pos = []
        self.turn = [1]
        self.boller = []
        self.krydser = []

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

    # Well, yea. The rest probably don't need commenting
    def nextTurn(self):
        if self.turn[0] == 1:
            self.turn[0] = 0
        elif self.turn[0] == 0:
            self.turn[0] = 1

    def addpos(self, content):
        self.pos.append(content)

    def getPos(self):
        return self.pos

    def getTurn(self):
        return self.turn[0]

    def getPos(self):
        return self.pos

    def getBolle(self):
        return self.boller

    def getKryds(self):
        return self.krydser
