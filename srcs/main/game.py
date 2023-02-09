from srcs.main.landmine import Landmine


class Game:
    def __init__(self, height, width, number_of_landmine):
        self.height = height
        self.width = width
        self.landmines = Landmine(number_of_landmine)
        self.map = []
        self.background_char = 'o'

    def clear_map(self):
        for i in range(0, self.height):
            self.map.append([self.background_char] * self.width)

    def init_map(self):
        self.clear_map()
        self.landmines.get_locations(self.height, self.width)
        for i in self.landmines.locations:
            self.map[int(i / self.height)][i % self.width] = self.landmines.char

    def print_map(self):
        for i in range(0, self.height):
            print(*self.map[i])

