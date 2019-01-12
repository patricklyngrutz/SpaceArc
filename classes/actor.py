import classes


class Actor():
    def __init__(self, name='Testronaut', items: "list" = None, effects: "list" = None, **kwargs):
        self.name = name
        self.base_stats = classes.Stat(**kwargs)
        if items is None:
            self.items = []
        if effects is None:
            self.effects = []

    def __iadd__(self, other):

        if type(other) == classes.Item:
            self.items.append(other)
            return self
        elif type(other) == classes.Effect:
            self.effects.append(other)
            return self
        elif type(other) == classes.Stat:
            self.base_stats += other
            return self

    def __isub__(self, other):
        if type(other) == classes.Item:
            self.items.remove(other)
            return self
        elif type(other) == classes.Effect:
            self.effects.remove(other)
            return self
        elif type(other) == classes.Stat:
            self.base_stats -= other
            return self

    @property
    def stats(self):
        return (
            classes.Stat.combine(
                self.base_stats,
                *self.items,
                *self.effects
            )
        )


#    @property
#    def __getitem__(self, item):
# todo: getitem and isub


if __name__ == '__main__':
    hero = Actor('Testronaut', intellect=1, strength=1)
    hero += classes.Item('Hat', tenacity=2)
    hero += classes.Stat(speed=9)
    hero += classes.Effect('Happy')
    print(hero.stats)
    print(hero.__dict__)
