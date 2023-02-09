import unittest
from srcs.main.game import Game


class MyTestGame(unittest.TestCase):
    def test_init_game(self):
        game = Game(5, 7, 3)

        self.assertEqual(game.height, 5)
        self.assertEqual(game.width, 7)

    def test_clear_map(self):
        game = Game(2, 3, 3)

        game.clear_map()

        self.assertEqual(game.map, [[game.background_char] * game.width] * game.height)


if __name__ == '__main__':
    unittest.main()
