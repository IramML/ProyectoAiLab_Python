class Hability:

    def __init__(self, name, normal_damange, advantage_damange, disventage_damange, normal_boost_damange, advantage_boost_damange, disventage_boost_damange, is_booster=False, turns_delay=0, booster_last=0) -> None:
        self.name = name
        self.normal_damange = normal_damange
        self.advantage_damange = advantage_damange
        self.disventage_damange = disventage_damange
        self.normal_boost_damange = normal_boost_damange
        self.advantage_boost_damange = advantage_boost_damange
        self.disventage_boost_damange = disventage_boost_damange
        self.turns_delay = turns_delay
        self.cumulative_turns_until_used = turns_delay + 1
        self.is_booster = False
        self.booster_last = booster_last


    def use(self):
        self.cumulative_turns_until_used = 0
        return self

    def pass_turn(self):
        self.cumulative_turns_until_used += 1

    def can_be_used(self):
        if self.turns_delay > 0:
            return self.cumulative_turns_until_used > self.turns_delay
        return True

    def did_booster_expired(self):
        if self.is_booster:
            return self.cumulative_turns_until_used > self.booster_last
        return True
