from src.lib.strategies.basestrategy import BaseStrategy

class HardcodedStrategy(BaseStrategy):
    def _loadConfig(self,config):
        self.sprinklerlocations = config["sprinklers"]

    def executeStrategy(self,field):
        retField = field.clone()

        for sprinklername in self.sprinklerlocations.keys():
            sprinkler = self.sprinklers[sprinklername]()
            for sprinklerlocation in self.sprinklerlocations[sprinklername]:
                self.logger.info(sprinklerlocation)
                retField.placeSprinkler(sprinkler, (sprinklerlocation['x'], sprinklerlocation['y']))

        return retField