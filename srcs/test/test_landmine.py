import unittest
from srcs.main.landmine import Landmine


class MyTestLandmine(unittest.TestCase):
    def test_init_landmine(self):
        landmine = Landmine(5)
        self.assertEqual(landmine.number, 5)

    def test_get_random_location(self):
        pass


if __name__ == '__main__':
    unittest.main()
