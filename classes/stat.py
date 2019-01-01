class Stat():
    """
    Represents core stats used in gameplay
    """

    core_stats = ['intellect', 'tenacity', 'strength', 'speed']

    def __init__(self,
                 intellect=0,
                 tenacity=0,
                 strength=0,
                 speed=0
                 ):
        self.intellect = int(intellect)
        self.tenacity = int(tenacity)
        self.strength = int(strength)
        self.speed = int(speed)

    def __repr__(self):
        return(f"Stat({self.intellect}, {self.tenacity}, {self.strength}, {self.speed})")

    def __add__(self, other: "Stat"):

        return(Stat(*[getattr(self, _, 0) + getattr(other, _, 0) for _ in Stat.core_stats]))