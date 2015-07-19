from pets.Pet import Pet


class Dog(Pet):
    def __init__(self, name, type):
        Pet.__init__(self, name, type)

    def __del__(self):
        Pet.__del__(self)

    def makesound(self):
        self.logger.info(str(self))


class Shepherd(Dog):
    def __init__(self, name):
        Dog.__init__(self, name, "Shepherd")

    def makesound(self):
        Dog.makesound(self)
        self.logger.info(">>> Shepherd bark~")


class Hound(Dog):
    def __init__(self, name):
        Dog.__init__(self, name, "Hound")

    def makesound(self):
        Dog.makesound(self)
        self.logger.info(">>> Hound barks~")