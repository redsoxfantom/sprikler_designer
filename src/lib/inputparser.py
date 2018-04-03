import json
from src.lib.sprinklers.factory import createsprinkler
from src.lib.field import Field
from src.lib.scorers.scorekeeper import ScoreKeeper
from src.lib.strategies.manager import StrategyManager


class InputParser:
    def __init__(self, filename):
        loadedfile = json.load(open(filename))

        self.sprinklers = {}
        for sprinkler in loadedfile['sprinklers']:
            self.sprinklers[sprinkler] = createsprinkler(sprinkler)

        self.originalfield = Field(loadedfile["field"])

        self.scorekeeper = ScoreKeeper(loadedfile["weights"])

        self.strategymanager = StrategyManager(loadedfile["strategies"], self.scorekeeper, self.sprinklers)