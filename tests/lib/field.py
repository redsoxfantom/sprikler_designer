from src.lib.field import Field
from src.lib.field import FieldValue
from tests.basetestclass import BaseTestClass
from tests.basetestclass import test
from src.lib.sprinklers.level1sprinkler import Level1Sprinkler
from tests.asserts import *


class FieldTest(BaseTestClass):

    @test
    def test_full_field(self):
        field = Field([
            ["X", "X"],
            ["X", "X"]
        ])
        equals(2,len(field.field))
        equals(2,len(field.field[0]))
        equals(2,len(field.field[1]))
        equals(FieldValue.available,field.field[0][0])
        equals(FieldValue.available,field.field[1][0])
        equals(FieldValue.available,field.field[0][1])
        equals(FieldValue.available,field.field[1][1])

    @test
    def test_partial_field(self):
        field = Field([
            [" ", "X"],
            ["X", "X"]
        ])
        equals(2, len(field.field))
        equals(2, len(field.field[0]))
        equals(2, len(field.field[1]))
        equals(FieldValue.unavailable,field.field[0][0])
        equals(FieldValue.available,field.field[1][0])
        equals(FieldValue.available,field.field[0][1])
        equals(FieldValue.available,field.field[1][1])

    @test
    def test_clone_field(self):
        field = Field([
            [" ", "X"],
            ["X", "X"]
        ])
        field.placeSprinkler(Level1Sprinkler(), (1, 1))
        field2 = field.clone()
        equals(2, len(field2.field))
        equals(2, len(field2.field[0]))
        equals(2, len(field2.field[1]))
        equals(FieldValue.unavailable, field2.field[0][0])
        equals(FieldValue.wet, field2.field[1][0])
        equals(FieldValue.wet, field2.field[0][1])
        equals(FieldValue.sprinkler, field2.field[1][1])
        notequals(field, field2)
        notequals(field.sprinklers, field2.sprinklers)



    @test
    def test_place_1_sprinkler_center(self):
        field = Field([
            ["X", "X", "X"],
            ["X", "X", "X"],
            ["X", "X", "X"]
        ])
        sprinkler = Level1Sprinkler()
        field.placeSprinkler(sprinkler, (1, 1))
        equals(FieldValue.available, field.field[0][0])
        equals(FieldValue.wet, field.field[1][0])
        equals(FieldValue.available, field.field[2][0])
        equals(FieldValue.wet, field.field[0][1])
        equals(FieldValue.sprinkler, field.field[1][1])
        equals(FieldValue.wet, field.field[2][1])
        equals(FieldValue.available, field.field[0][2])
        equals(FieldValue.wet, field.field[1][2])
        equals(FieldValue.available, field.field[2][2])
        equals(1, len(field.sprinklers))
        equals(sprinkler, field.sprinklers[0])

    @test
    def test_place_1_sprinkler_offset(self):
        field = Field([
            ["X", "X", "X"],
            ["X", "X", "X"],
            ["X", "X", "X"]
        ])
        sprinkler = Level1Sprinkler()
        field.placeSprinkler(sprinkler, (0, 1))
        equals(FieldValue.wet, field.field[0][0])
        equals(FieldValue.available, field.field[1][0])
        equals(FieldValue.available, field.field[2][0])
        equals(FieldValue.sprinkler, field.field[0][1])
        equals(FieldValue.wet, field.field[1][1])
        equals(FieldValue.available, field.field[2][1])
        equals(FieldValue.wet, field.field[0][2])
        equals(FieldValue.available, field.field[1][2])
        equals(FieldValue.available, field.field[2][2])
        equals(1, len(field.sprinklers))
        equals(sprinkler, field.sprinklers[0])

    @test
    def test_place_2_sprinklers_same_spot(self):
        field = Field([
            ["X", "X", "X"],
            ["X", "X", "X"],
            ["X", "X", "X"]
        ])
        sprinkler = Level1Sprinkler()
        sprinkler2 = Level1Sprinkler()
        field.placeSprinkler(sprinkler, (0, 1))
        field.placeSprinkler(sprinkler2, (0, 1))
        equals(FieldValue.wet, field.field[0][0])
        equals(FieldValue.available, field.field[1][0])
        equals(FieldValue.available, field.field[2][0])
        equals(FieldValue.sprinkler, field.field[0][1])
        equals(FieldValue.wet, field.field[1][1])
        equals(FieldValue.available, field.field[2][1])
        equals(FieldValue.wet, field.field[0][2])
        equals(FieldValue.available, field.field[1][2])
        equals(FieldValue.available, field.field[2][2])
        equals(1, len(field.sprinklers))
        equals(sprinkler, field.sprinklers[0])

    @test
    def test_place_2_sprinklers_different_spots(self):
        field = Field([
            ["X", "X", "X"],
            ["X", "X", "X"],
            ["X", "X", "X"]
        ])
        sprinkler = Level1Sprinkler()
        sprinkler2 = Level1Sprinkler()
        field.placeSprinkler(sprinkler, (0, 1))
        field.placeSprinkler(sprinkler2, (2, 0))
        equals(FieldValue.wet, field.field[0][0])
        equals(FieldValue.wet, field.field[1][0])
        equals(FieldValue.sprinkler, field.field[2][0])
        equals(FieldValue.sprinkler, field.field[0][1])
        equals(FieldValue.wet, field.field[1][1])
        equals(FieldValue.wet, field.field[2][1])
        equals(FieldValue.wet, field.field[0][2])
        equals(FieldValue.available, field.field[1][2])
        equals(FieldValue.available, field.field[2][2])
        equals(2, len(field.sprinklers))
        istrue(sprinkler in field.sprinklers)
        istrue(sprinkler2 in field.sprinklers)

    @test
    def test_place_1_sprinkler_off_map(self):
        field = Field([
            ["X", "X", "X"],
            ["X", "X", "X"],
            ["X", "X", "X"]
        ])
        sprinkler = Level1Sprinkler()
        field.placeSprinkler(sprinkler, (-1, -1))
        equals(FieldValue.available, field.field[0][0])
        equals(FieldValue.available, field.field[1][0])
        equals(FieldValue.available, field.field[2][0])
        equals(FieldValue.available, field.field[0][1])
        equals(FieldValue.available, field.field[1][1])
        equals(FieldValue.available, field.field[2][1])
        equals(FieldValue.available, field.field[0][2])
        equals(FieldValue.available, field.field[1][2])
        equals(FieldValue.available, field.field[2][2])
        equals(0, len(field.sprinklers))

    @test
    def test_place_1_sprinkler_on_unavailable(self):
        field = Field([
            [" ", "X", "X"],
            ["X", "X", "X"],
            ["X", "X", "X"]
        ])
        sprinkler = Level1Sprinkler()
        field.placeSprinkler(sprinkler, (0, 0))
        equals(FieldValue.unavailable, field.field[0][0])
        equals(FieldValue.available, field.field[1][0])
        equals(FieldValue.available, field.field[2][0])
        equals(FieldValue.available, field.field[0][1])
        equals(FieldValue.available, field.field[1][1])
        equals(FieldValue.available, field.field[2][1])
        equals(FieldValue.available, field.field[0][2])
        equals(FieldValue.available, field.field[1][2])
        equals(FieldValue.available, field.field[2][2])
        equals(0, len(field.sprinklers))
