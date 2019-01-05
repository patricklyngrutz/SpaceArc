import classes.stat


class Effect(classes.stat.Stat):

    def __init__(self, name='Effect', **kwargs):
        self.name = name
        super().__init__(**kwargs)

    def __repr__(self):
        return (f"Effect(\"{self.name}\")")