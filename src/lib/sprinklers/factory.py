from .level1sprinkler import Level1Sprinkler


def createsprinkler(sprinklername):
    sprinklerswitch = {
        "Level1": Level1Sprinkler
    }
    return sprinklerswitch.get(sprinklername, "Invalid sprinkler name")
