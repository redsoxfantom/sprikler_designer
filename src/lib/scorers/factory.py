from src.lib.scorers.numwetpatchesscorer import NumWetPatchesScorer
from src.lib.scorers.numdrypatchesscorer import NumDryPatchesScorer
from src.lib.scorers.numplantablepatchesscorer import NumPlantablePatchesScorer
from src.lib.scorers.numsprinklersscorer import NumSprinklersScorer
from src.lib.scorers.basescorer import BaseScorer


def createScorer(scorername, scorerweight):
    scorerswitch = {
        "numWetPatches": NumWetPatchesScorer,
        "numDryPatches": NumDryPatchesScorer,
        "numPlantablePatches": NumPlantablePatchesScorer,
        "numSprinklers": NumSprinklersScorer
    }
    scorer = scorerswitch.get(scorername, BaseScorer)
    return scorer(scorerweight)