from src.lib.scorers.basescorer import BaseScorer
from src.lib.field import FieldValue


class NumDryPatchesScorer(BaseScorer):
    def _calculateScore(self, fieldVal):
        if fieldVal == FieldValue.available:
            return 1
        else:
            return 0
