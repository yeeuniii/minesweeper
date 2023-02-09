import random


class Landmine:
    def __init__(self, number_of_landmines):
        self.number = number_of_landmines
        self.char = '*'
        self.locations = list()

    def get_location(self, height, width):
        value = random.randrange(0, height * width)
        while value in self.locations:
            value = random.randrange(0, height * width)
        return value

    def get_locations(self, height, width):
        for i in range(0, self.number):
            self.locations.append(self.get_location(height, width))