from src.lib.scorers.factory import createScorer


class ScoreKeeper:
    def __init__(self, weights):
        self.scorers = []
        for weight in weights:
            self.scorers.append(createScorer(weight, weights[weight]))

    def calculateScore(self, field):
        score = 0
        for scorer in self.scorers:
            score += scorer.calculateScore(field.field)
        return score