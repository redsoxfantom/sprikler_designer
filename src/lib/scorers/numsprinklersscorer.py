from src.lib.scorers.basescorer import BaseScorer
from src.lib.field import FieldValue


class NumSprinklersScorer(BaseScorer):
    def _calculateScore(self, fieldVal):
        if fieldVal == FieldValue.sprinkler:
            return 1
        else:
            return 0
