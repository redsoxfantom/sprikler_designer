from tests.basetestclass import BaseTestClass
from tests.basetestclass import test
from tests.asserts import *
from src.lib.scorers.scorekeeper import ScoreKeeper
from src.lib.field import Field
from src.lib.sprinklers.level1sprinkler import Level1Sprinkler


class ScoreKeeperTest(BaseTestClass):

    @test
    def test_create_scorekeeper(self):
        scorekeeper = ScoreKeeper({
            "numWetPatches": 1.0,
            "numDryPatches": 0.5
        })
        equals(2, len(scorekeeper.scorers))

    @test
    def test_score_field(self):
        scorekeeper = ScoreKeeper({
            "numWetPatches": 1.0,
            "numDryPatches": 0.5
        })
        field = Field([
            [" ", "X", "X"],
            ["X", "X", "X"],
            ["X", "X", "X"]
        ])
        sprinkler = Level1Sprinkler()
        field.placeSprinkler(sprinkler, (1, 1))
        score = scorekeeper.calculateScore(field)
        equals(5.5, score)