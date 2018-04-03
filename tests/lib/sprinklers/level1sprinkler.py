from tests.basetestclass import BaseTestClass
from tests.basetestclass import test
from src.lib.sprinklers.level1sprinkler import Level1Sprinkler
from tests.asserts import *


class Level1SprinklerTest(BaseTestClass):

    @test
    def set_position_test(self):
        sp = Level1Sprinkler()
        sp.setPosition((5, 5))
        equals((5, 5), sp.getPosition())

    @test
    def get_wet_squares_test(self):
        sp = Level1Sprinkler()
        sp.setPosition((10, 10))
        istrue(sp.getIsWetSquare((9, 10)))
        istrue(sp.getIsWetSquare((10, 11)))
        istrue(sp.getIsWetSquare((11, 10)))
        istrue(sp.getIsWetSquare((10, 9)))

    @test
    def get_all_wet_squares_test(self):
        sp = Level1Sprinkler()
        sp.setPosition((10, 10))
        allWetSquares = sp.getAllWetSquares()
        equals(4, len(allWetSquares))
        equals((9, 10), allWetSquares[0])
        equals((10, 11), allWetSquares[1])
        equals((11, 10), allWetSquares[2])
        equals((10, 9), allWetSquares[3])