import classes

# TODO: iadd method to add items, effects, modify stats


class Actor():
    def __init__(self, name='Testronaut', items: "list" = None, effects: "list" = None, **kwargs):
        self.name = name
        self.stat = classes.Stat(**kwargs)
        if items is None:
            self.items = []
        if effects is None:
            self.effects = []

    def __iadd__(self, other):
        if type(other) == classes.Item:
            self.items.append(other)
        elif type(other) == classes.Effect:
            self.effects.append(other)
        elif type(other) == classes.Stat:
            self.stat += other


if __name__ == '__main__':
    print('ok')
    hero = Actor('Testronaut', intellect=1, strength=1)
    hero += classes.Item('Hat', tenacity=2)
    #hero += classes.Stat(speed=9)
    #hero += classes.Effect('happy dude')

    print(hero.__dict__)
