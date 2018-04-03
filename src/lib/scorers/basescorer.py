class BaseScorer:
    def __init__(self, weight):
        self.weight = weight

    def calculateScore(self,field):
        count = 0
        for x in range(0, len(field)):
            for y in range(0, len(field[x])):
                count += self._calculateScore(field[x][y])
        count *= self.weight
        return count

    def _calculateScore(self, fieldVal):
        return 0
