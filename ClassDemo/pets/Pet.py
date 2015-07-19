from abc import abstractmethod

from common.Whisper import Whisper


class Pet(object):
    def __init__(self, name, type):
        self.name = name
        self.type = type

        self.logger = Whisper.getLogger()
        self.logger.info(">>> init pet...")

    def __del__(self):
        self.logger.info(">>> del pet...")

    def __str__(self):
        return "name: %s, type: %s" % (self.name, self.type)

    def __eq__(self, other):
        if not isinstance(other, Pet):
            return False
        return self.name == other.name and self.name == other.type

    @abstractmethod
    def makesound(self):
        pass
