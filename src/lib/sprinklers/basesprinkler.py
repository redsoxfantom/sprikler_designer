class BaseSprinkler:
    def __init__(self, listofwetsquares):
        self.listofwetsquares = listofwetsquares
        self.position = (0, 0)

    def setPosition(self,position):
        self.position = position
        newlistofwetsquares = []
        # Iterate over the list of wet squares we had before, calculating where the
        # wet squares would be when we offset from our position
        for wetsquare in self.listofwetsquares:
            newlistofwetsquares.append((wetsquare[0]+position[0], wetsquare[1]+position[1]))
        self.listofwetsquares = newlistofwetsquares

    def getPosition(self):
        return self.position

    def getIsWetSquare(self,position):
        return position in self.listofwetsquares

    def getAllWetSquares(self):
        return self.listofwetsquares

    def getIcon(self):
        return "?"
