
from domain.advantage_level import AdvantageLevel


class Fighter:
    def __init__(self, fighter_type, health_points, habilities) -> None:
        self.fighter_type = fighter_type
        self.health_points = health_points
        self.habilities = habilities
        self.has_booster = False

    def receive_power(self, fighter, hability):
        if hability.is_booster:
            fighter.has_booster = True
            return
        advantage_level = fighter.fighter_type.get_advantage_level(self.fighter_type)
        if advantage_level == AdvantageLevel.ADVANTAGE:
            self.health_points -= hability.advantage_boost_damange if fighter.has_booster else hability.advantage_damange
        elif advantage_level == AdvantageLevel.WEAKNESS:
            self.health_points -= hability.disventage_boost_damange if fighter.has_booster else hability.disventage_damange
        else:
            self.health_points -= hability.normal_boost_damange if fighter.has_booster else hability.normal_damange
            



