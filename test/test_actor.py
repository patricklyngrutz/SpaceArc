from unittest import TestCase
import classes


class TestActor(TestCase):
    def setUp(self):
        self.actor1 = classes.Actor("Cosmopal")
        self.actor1.base_stats = classes.Stat(4, 3, 2, 1)

    def test_pick_up_item(self):
        self.assertTrue(self.actor1.items == [])
        self.actor1 += classes.Item('Hat')
        self.assertTrue(classes.Item('Hat') in self.actor1.items)

    def test_drop_item(self):
        self.hat = classes.Item('hat')
        self.assertTrue(self.hat not in self.actor1.items)
        self.actor1 += self.hat
        self.assertTrue(self.hat in self.actor1.items)
        self.actor1 -= self.hat
        self.assertTrue(self.hat not in self.actor1.items)