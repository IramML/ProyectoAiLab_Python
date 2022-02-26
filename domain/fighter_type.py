from enum import Enum

from domain.advantage_level import AdvantageLevel

class FighterType(Enum):
    WATER = 0
    FIRE = 1
    ELECTRIC = 2
    PLANT = 3
    SCARAB = 4
    ROCK = 5

    def to_string(self):
        switch = {
            FighterType.WATER: "Agua",
            FighterType.FIRE: "Fuego",
            FighterType.ELECTRIC: "Electrico",
            FighterType.SCARAB: "Escarabo",
            FighterType.PLANT: "Planta",
            FighterType.ROCK: "Roca",
        }
        return switch.get(self)

    def get_advantage_level(self, fighter_type):
        if fighter_type in self.get_advantages(): 
            return AdvantageLevel.ADVANTAGE

        if fighter_type in self.get_weakness():
            return AdvantageLevel.WEAKNESS 
        
        return AdvantageLevel.NORMAL

    def get_advantages(self):
        switch = {
            FighterType.WATER: [FighterType.ROCK, FighterType.FIRE],
            FighterType.FIRE: [FighterType.PLANT, FighterType.SCARAB],
            FighterType.ELECTRIC: [FighterType.WATER, FighterType.SCARAB],
            FighterType.SCARAB: [FighterType.PLANT, FighterType.ROCK],
            FighterType.PLANT: [FighterType.ROCK, FighterType.WATER, FighterType.ELECTRIC],
            FighterType.ROCK: [FighterType.FIRE, FighterType.ELECTRIC],
        }
        return switch.get(self)

    def get_normal(self):
        switch = {
            FighterType.WATER: [FighterType.WATER, FighterType.SCARAB],
            FighterType.FIRE: [FighterType.FIRE, FighterType.ELECTRIC],
            FighterType.ELECTRIC: [FighterType.ELECTRIC, FighterType.FIRE],
            FighterType.SCARAB: [FighterType.SCARAB, FighterType.WATER],
            FighterType.PLANT: [FighterType.PLANT],
            FighterType.ROCK: [FighterType.ROCK, FighterType.SCARAB],
        }
        return switch.get(self)
        
    def get_weakness(self):
        switch = {
            FighterType.WATER: [FighterType.ELECTRIC, FighterType.PLANT],
            FighterType.FIRE: [FighterType.WATER, FighterType.ROCK],
            FighterType.ELECTRIC: [FighterType.ROCK, FighterType.PLANT],
            FighterType.SCARAB: [FighterType.FIRE, FighterType.ELECTRIC],
            FighterType.PLANT: [FighterType.FIRE, FighterType.SCARAB],
            FighterType.ROCK: [FighterType.WATER, FighterType.PLANT],
        }
        return switch.get(self)