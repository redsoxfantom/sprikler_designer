from src.lib.scorers.basescorer import BaseScorer
from src.lib.field import FieldValue


class NumPlantablePatchesScorer(BaseScorer):
    def _calculateScore(self, fieldVal):
        if fieldVal == FieldValue.wet or fieldVal == FieldValue.available:
            return 1
        else:
            return 0
