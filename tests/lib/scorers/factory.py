from tests.basetestclass import BaseTestClass
from tests.basetestclass import test
from tests.asserts import *
from src.lib.scorers.factory import createScorer


class ScorerFactoryTest(BaseTestClass):

    @test
    def test_create_unknown_scorer(self):
        scorer = createScorer("UNKNOWN", 1.0)
        istrue('BaseScorer' in scorer.__class__.__name__)
        equals(1.0, scorer.weight)

    @test
    def test_create_num_plantable_scorer(self):
        scorer = createScorer("numPlantablePatches", 0.0)
        istrue('NumPlantablePatchesScorer' in scorer.__class__.__name__)

    @test
    def test_create_num_wet_scorer(self):
        scorer = createScorer("numWetPatches", 0.0)
        istrue('NumWetPatchesScorer' in scorer.__class__.__name__)

    @test
    def test_create_num_dry_scorer(self):
        scorer = createScorer("numDryPatches", 0.0)
        istrue('NumDryPatchesScorer' in scorer.__class__.__name__)

    @test
    def test_create_num_sprinklers_scorer(self):
        scorer = createScorer("numSprinklers", 0.0)
        istrue('NumSprinklersScorer' in scorer.__class__.__name__)
