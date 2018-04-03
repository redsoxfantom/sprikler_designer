from tests.lib.inputparser import InputParserTest
from tests.lib.sprinklers.level1sprinkler import Level1SprinklerTest
from tests.lib.field import FieldTest
from tests.lib.scorers.factory import ScorerFactoryTest
from tests.lib.scorers.scorer import ScorerTest
from tests.lib.scorers.scorekeeper import ScoreKeeperTest


totals = (0, 0)

tests = [
    InputParserTest(),
    Level1SprinklerTest(),
    FieldTest(),
    ScorerFactoryTest(),
    ScorerTest(),
    ScoreKeeperTest()
]

for test in tests:
    newvals = test.run_tests()
    totals = (totals[0]+newvals[0], totals[1]+newvals[1])
    print("")

print("All tests complete (%s/%s passed)" % (totals))
