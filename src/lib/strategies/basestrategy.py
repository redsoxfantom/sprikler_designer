import logging


class BaseStrategy:
    def __init__(self, config, scorer, sprinklers):
        self.scorer = scorer
        self.sprinklers = sprinklers
        self.logger = logging.getLogger(self.__class__.__name__)
        self._loadConfig(config)

    def _loadConfig(self,config):
        pass

    def executeStrategy(self,field):
        return field.clone()