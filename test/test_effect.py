import unittest
from classes import Effect

class test_Effect(unittest.TestCase):
    def setUp(self):
        self.effect1 = Effect('Happy', tenacity = 1)
        self.effect2 = Effect('Sad', tenacity = -1)

    def test_init(self):
        assert(self.effect1.name == 'Happy')
        assert(self.effect1.tenacity == 1)
        assert(self.effect1.strength == 0)