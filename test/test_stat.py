import unittest
from classes.stat import Stat


class test_Stats(unittest.TestCase):
    def setUp(self):
        self.stats1 = Stat(1,2,3,4)
        self.stats2 = Stat(1,0,1,0)

    def test_add(self):
        self.stats3 = self.stats1 + self.stats2
        self.assertTrue(self.stats3.intellect==2)