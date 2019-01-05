import unittest
from classes import Item

class test_Item(unittest.TestCase):
    def setUp(self):
        self.item1 = Item('Sword', strength=1)
        self.item2 = Item('Book', intellect=1)

    def test_init(self):
        assert(self.item1.name == 'Sword')
        assert(self.item1.strength == 1)