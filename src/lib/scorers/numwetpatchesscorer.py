from src.lib.scorers.basescorer import BaseScorer
from src.lib.field import FieldValue


class NumWetPatchesScorer(BaseScorer):
    def _calculateScore(self, fieldVal):
        if fieldVal == FieldValue.wet:
            return 1
        else:
            return 0
