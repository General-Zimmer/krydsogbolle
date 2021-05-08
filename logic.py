import data as data


class logi:
    def __init__(self):
        self.data = data.data()

    def CheckWin(self, player: str):
        score = None

        # Get sorted list of the data to be checked
        if player == "kryds":
            score = sorted(self.data.getKryds())
        elif player == "bolle":
            score = sorted(self.data.getBolle())

        # You can't win if you don't have 3 scores
        if len(score) != 3:
            return None
        print(score)
        middle = score[1]
        # First check the middle score for vertical victories
        if middle == 1 or middle == 4 or middle == 7:
            # Check if the first and last score is in the correct place
            if score[1] == (score[0] + 1) and score[1] == (score[2] - 1):
                print(player + " vandt")
                return player
        # Then check the middle score for horrizontel victories
        if middle == 3 or middle == 4 or middle == 5:
            # Check if the first and last score is in the correct place
            if score[1] == (score[0] + 3) and score[1] == (score[2] - 3):
                print(player + " vandt")
                return player
        # Last check the middle score for diagonal victories
        if middle == 4:
            # Check if the first and last score is in the correct place
            if score[1] == (score[0] + 4) and score[1] == (score[2] - 4) or score[1] == (score[0] + 2) and score[1] == (
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

    def NextTurn(self):
        self.data.nextTurn()

    def GetTurn(self):
        return self.data.turn[0]


