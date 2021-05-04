import data as data


class logi:
    def __init__(self):
        self.data = data.data()

    def CheckWin(self, player: str):
        score = None
        if player == "kryds":
            score = sorted(self.data.getKryds())
        elif player == "bolle":
            score = sorted(self.data.getBolle())

        if len(score) != 3:
            return None

        if score[1] == 1 or 4 or 7:
            if score[1] == (score[0] + 1) and score[1] == (score[2] - 1):
                print(player + " vandt")
                return player
        if score[1] == 3 or 4 or 5:
            if score[1] == (score[0] + 3) and score[1] == (score[2] - 3):
                print(player + " vandt")
                return player
        if score[1] == 4:
            if score[1] == (score[0] + 4) and score[1] == (score[2] - 4) or score[1] == (score[0] + 2) and score[1] == (
                    score[2] - 2):
                print(player + " vandt")
                return player
        return None

    def StorePos(self, content):
        self.data.addpos(content)

    def getBolle(self):
        return self.data.getBolle()

    def getKryds(self):
        return self.data.getKryds()

    def NextTurn(self):
        self.data.nextTurn()

    def GetTurn(self):
        return self.data.turn[0]

    def SetScore(self, player, num, button=None):
        return self.data.Setscore(player, num, button)
