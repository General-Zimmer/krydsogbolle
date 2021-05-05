class data:
    def __init__(self):
        self.pos = []
        self.turn = [1]
        self.boller = []
        self.krydser = []

    def Setscore(self, player: str, num: int, button):
        result = None
        if player == "bolle":
            if button is not None:
                self.boller.remove(button)
                return
            self.boller.append(num)
            if len(self.boller) >= 4:
                result = self.boller[0]
                self.boller.pop(0)
        elif player == "kryds":
            if button is not None:
                self.krydser.remove(button)
                return
            self.krydser.append(num)
            if len(self.krydser) >= 4:
                result = self.krydser[0]
                self.krydser.pop(0)
        return result

    def nextTurn(self):
        if self.turn[0] == 1:
            self.turn[0] = 0
        elif self.turn[0] == 0:
            self.turn[0] = 1

    def addpos(self, content):
        self.pos.append(content)

    def getTurn(self):
        return self.turn[0]

    def getPos(self):
        return self.pos

    def getBolle(self):
        return self.boller

    def getKryds(self):
        return self.krydser
