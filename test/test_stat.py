import unittest
from classes import Stat


class test_Stats(unittest.TestCase):
    def setUp(self):
        self.stats1 = Stat(1, 2, 3, 4)
        self.stats2 = Stat(1, 0, 1, 0)
        self.stats3 = Stat(-1, -1, -1, -99)

    def test_add(self):
        self.stats4 = self.stats1 + self.stats2
        self.assertTrue(self.stats4.intellect == 2)
        self.assertTrue((self.stats3 + self.stats2).speed == -99)

    def test_combine(self):
        self.assertTrue(
            Stat.combine(self.stats1, self.stats2, self.stats3) ==
            Stat(1, 1, 3, -95)
        )
