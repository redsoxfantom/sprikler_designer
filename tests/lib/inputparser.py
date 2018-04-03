from tests.basetestclass import BaseTestClass
from tests.basetestclass import test
from src.lib.inputparser import InputParser
from src.lib.sprinklers.level1sprinkler import Level1Sprinkler
from src.lib.field import FieldValue
from tests.asserts import *


class InputParserTest(BaseTestClass):

    @test
    def test_load_sprinklers(self):
        parser = InputParser(self.testroot + "/resources/simplefield.json")
        istrue("Level1" in parser.sprinklers.keys())
        equals(parser.sprinklers["Level1"], Level1Sprinkler)

    @test
    def test_load_field(self):
        parser = InputParser(self.testroot + "/resources/simplefield.json")
        equals(FieldValue.available, parser.originalfield.field[0][0])
        equals(FieldValue.available, parser.originalfield.field[1][0])
        equals(FieldValue.available, parser.originalfield.field[2][0])
        equals(FieldValue.available, parser.originalfield.field[0][1])
        equals(FieldValue.available, parser.originalfield.field[1][1])
        equals(FieldValue.available, parser.originalfield.field[2][1])
        equals(FieldValue.available, parser.originalfield.field[0][2])
        equals(FieldValue.available, parser.originalfield.field[1][2])
        equals(FieldValue.available, parser.originalfield.field[2][2])
