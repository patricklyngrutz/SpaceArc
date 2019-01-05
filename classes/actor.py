import classes.stat

class Actor():
    def __init__(self, name = 'Testronaut', items: "List" = None, effects: "List" = None, **kwargs):
        self.name = name
        self.stat = classes.stat.Stat(**kwargs)
        if self.items is None:
            self.items = []
        if self.effects is None:
            self.effects = []