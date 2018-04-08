from src.lib.strategies.basestrategy import BaseStrategy
import random


class RandomStrategy(BaseStrategy):
    def _loadConfig(self, config):
        self.iterations = config['iterations']
        self.numFieldsPerIteration = config['numFieldsPerIteration']

    def executeStrategy(self, field):
        currentBestScore = self.scorer.calculateScore(field)
        currentBestField = field.clone()
        maxX = len(field.field)-1
        maxY = len(field.field[0])-1
        sprinklers = list(self.sprinklers.values())
        numFields = self.iterations * self.numFieldsPerIteration
        currentFieldCount = 0
        self.logger.info("Generating %s fields..." % numFields)

        for iteration in range(0,self.iterations):
            self.logger.debug("Starting iteration %s" % iteration)
            self.logger.debug("Current best field: %s" % currentBestField.getFieldStrings())
            bestFieldThisIteration = currentBestField.clone()
            bestScoreThisIteration = currentBestScore

            for fieldCount in range(0,self.numFieldsPerIteration):
                self.logger.debug("Creating field %s for iteration %s" % (fieldCount,iteration))
                newField = currentBestField.clone()
                sprinkler = sprinklers[random.randint(0, len(sprinklers)-1)]()
                newField.placeSprinkler(sprinkler, (random.randint(0, maxX), random.randint(0, maxY)))
                score = self.scorer.calculateScore(newField)
                if score > bestScoreThisIteration:
                    bestScoreThisIteration = score
                    bestFieldThisIteration = newField
                currentFieldCount += 1
                if currentFieldCount % 1000 == 0:
                    self.logger.info("Generated %s fields. %s percent complete" % (currentFieldCount, (currentFieldCount / numFields) * 100))

            currentBestScore = bestScoreThisIteration
            currentBestField = bestFieldThisIteration

        return currentBestField
