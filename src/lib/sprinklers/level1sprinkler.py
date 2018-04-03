from .basesprinkler import BaseSprinkler


class Level1Sprinkler(BaseSprinkler):
    def __init__(self):
        BaseSprinkler.__init__(self, ((-1, 0), (0, 1), (1, 0), (0, -1)))

    def getIcon(self):
        return "1"
