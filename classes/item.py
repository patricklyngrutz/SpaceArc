import classes.stat


class Item(classes.stat.Stat):

    def __init__(self, name='Item', temporary=True, **kwargs):
        self.name = name
        self.temporary=temporary
        super().__init__(**kwargs)

    def __repr__(self):
        return(f"Item(\"{self.name}\")")