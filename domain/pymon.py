from domain.fighter import Fighter


class Pymon(Fighter):

    def __init__(self, name, fighter_type, health_points, habilities) -> None:
        super().__init__(fighter_type=fighter_type, health_points=health_points, habilities=habilities)
        self.name = name

