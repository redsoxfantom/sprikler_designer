from tests.basetestclass import BaseTestClass
from tests.basetestclass import test
from tests.asserts import *
from src.lib.field import FieldValue
from src.lib.scorers.numdrypatchesscorer import NumDryPatchesScorer
from src.lib.scorers.numwetpatchesscorer import NumWetPatchesScorer
from src.lib.scorers.numsprinklersscorer import NumSprinklersScorer
from src.lib.scorers.numplantablepatchesscorer import NumPlantablePatchesScorer


class ScorerTest(BaseTestClass):

    @test
    def test_count_dry_patches(self):
        field = [
            [FieldValue.available, FieldValue.available],
            [FieldValue.sprinkler, FieldValue.wet]
        ]
        scorer = NumDryPatchesScorer(0.5)
        score = scorer.calculateScore(field)
        equals(1.0, score)

    @test
    def test_count_wet_patches(self):
        field = [
            [FieldValue.wet, FieldValue.available],
            [FieldValue.sprinkler, FieldValue.wet]
        ]
        scorer = NumWetPatchesScorer(1.0)
        score = scorer.calculateScore(field)
        equals(2.0, score)

    @test
    def test_count_sprinkler_patches(self):
        field = [
            [FieldValue.wet, FieldValue.available],
            [FieldValue.sprinkler, FieldValue.wet]
        ]
        scorer = NumSprinklersScorer(-0.5)
        score = scorer.calculateScore(field)
        equals(-0.5, score)

    @test
    def test_count_plantable_patches(self):
        field = [
            [FieldValue.wet, FieldValue.available],
            [FieldValue.sprinkler, FieldValue.wet]
        ]
        scorer = NumPlantablePatchesScorer(-1.0)
        score = scorer.calculateScore(field)
        equals(-3.0, score)