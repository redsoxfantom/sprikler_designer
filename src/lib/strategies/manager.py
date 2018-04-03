from src.lib.strategies.factory import createStrategy
import logging


class StrategyManager:
    def __init__(self,strategies, scorer, sprinklers):
        self.strategies = []
        self.scorer = scorer
        self.logger = logging.getLogger(self.__class__.__name__)
        for strategy in strategies:
            strat = createStrategy(strategy, scorer, sprinklers)
            self.strategies.append(strat)

    def executeStrategies(self, field):
        possibleFields = []
        for strategy in self.strategies:
            self.logger.info("Executing %s strategy..." % strategy.__class__.__name__)
            possibleFields.append(strategy.executeStrategy(field))
            self.logger.info("%s strategy complete" % strategy.__class__.__name__)
        currentBestScore = self.scorer.calculateScore(field)
        currentBestField = field
        for possibleField in possibleFields:
            score = self.scorer.calculateScore(possibleField)
            if score > currentBestScore:
                currentBestScore = score
                currentBestField = possibleField
        return currentBestScore, currentBestField