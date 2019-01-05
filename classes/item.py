import classes.stat


class Item(classes.stat.Stat):

    def __init__(self, name='Item', **kwargs):
        self.name = name
        super().__init__(**kwargs)

    def __repr__(self):
        return(f"Item(\"{self.name}\")")