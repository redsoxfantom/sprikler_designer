from enum import Enum
import logging
import copy


class FieldValue(Enum):
    unavailable = 0
    available = 1
    sprinkler = 2
    wet = 3

class Field:
    def __init__(self, fielddef=[]):
        self.field = []
        self.sprinklers = []
        self.logger = logging.getLogger(self.__class__.__name__)
        for x in range(0, len(fielddef)):
            self.field.append([])
            for y in range(0, len(fielddef[x])):
                if fielddef[x][y] == "X":
                    self.field[x].append(FieldValue.available)
                else:
                    self.field[x].append(FieldValue.unavailable)

    def clone(self):
        f2 = Field()
        f2.sprinklers = copy.deepcopy(self.sprinklers)
        for x in range(0, len(self.field)):
            f2.field.append([])
            for y in range(0, len(self.field[x])):
                f2.field[x].append(self.field[x][y])
        return f2

    def placeSprinkler(self, sprinkler, position):
        if position[0] < 0 or position[0] >= len(self.field[0]):
            return
        if position[1] < 0 or position[1] >= len(self.field):
            return
        if self.field[position[0]][position[1]] == FieldValue.sprinkler or self.field[position[0]][position[1]] == FieldValue.unavailable:
            return
        self.logger.debug("Placing sprinkler %s at location %s" % (sprinkler.__class__.__name__, position))

        sprinkler.setPosition(position)
        self.field[position[0]][position[1]] = FieldValue.sprinkler

        newWetSquares = sprinkler.getAllWetSquares()
        for wetsquare in newWetSquares:
            if wetsquare[0] < 0 or wetsquare[0] >= len(self.field[0]):
                continue
            if wetsquare[1] < 0 or wetsquare[1] >= len(self.field):
                continue
            if self.field[wetsquare[0]][wetsquare[1]] == FieldValue.available:
                self.field[wetsquare[0]][wetsquare[1]] = FieldValue.wet
        self.sprinklers.append(sprinkler)

    def getFieldStrings(self):
        strings = []
        for x in range(0,len(self.field)):
            strings.append([])
            for y in range(0,len(self.field[x])):
                val = self.field[x][y]
                if val == FieldValue.wet or val == FieldValue.available:
                    strings[x].append("X")
                elif val == FieldValue.unavailable:
                    strings[x].append(" ")
                elif val == FieldValue.sprinkler:
                    for sprinkler in self.sprinklers:
                        pos = sprinkler.getPosition()
                        if pos == (x, y):
                            strings[x].append(sprinkler.getIcon())
        return strings