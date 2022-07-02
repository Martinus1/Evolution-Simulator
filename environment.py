MAX_TIME = 1440
class Environment:
    def __init__(self, animals, minPerSec):
        self.animals = animals
        self.time = 0
        self.day = 0
        self.minPerSec = minPerSec

    def timeStep(self):
        self.time += self.minPerSec

        if self.time >= 1440:
            self.time %= 1440
            self.day += 1 

        hours = (self.time // 60)
        minutes = (self.time - hours * 60)

        print("DAY: " + str(self.day))
        print("TIME: " + str(hours) + ":" + str(minutes))