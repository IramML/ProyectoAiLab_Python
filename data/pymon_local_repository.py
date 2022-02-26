

from domain.fighter_type import FighterType
from domain.hability import Hability
from domain.pymon import Pymon


class PymonLocalRepository():
    def get_pymons(self):
        return [ Pymon('Aquarder', FighterType.WATER, 25, [Hability('Aqua-jet', 3,5,2,5,7,4), Hability('Cola férrea', 2,2,2,2,2,2), Hability('Cabezazo', 2,2,2,2,2,2), Hability('Lluvia', 0,0,0,0,0,0, turns_delay=3, booster_last=2, is_booster=True)]),
            Pymon('Firesor', FighterType.FIRE, 25, [Hability('Llamarada', 3,5,2,5,7,4), Hability('Embestida', 2,2,2,2,2,2), Hability('Mordisco', 2,2,2,2,2,2), Hability('Día soleado', 0,0,0,0,0,0, turns_delay=3, booster_last=2, is_booster=True)]),
            Pymon('Electder', FighterType.ELECTRIC, 25, [Hability('Trueno', 3,5,2,5,7,4), Hability('Arañazo', 3,3,3,3,3,3), Hability('Mordisco', 3,3,3,3,3,3), Hability('Campo magnético', 0,0,0,0,0,0, turns_delay=3, booster_last=2, is_booster=True)]),
            Pymon('Mousebug', FighterType.SCARAB, 25, [Hability('Picotazo', 3,5,2,5,7,4), Hability('Embestida', 2,2,2,2,2,2), Hability('Cabezazo',2,2,2,2,2,2), Hability('Esporas', 0,0,0,0,0,0, turns_delay=3, booster_last=2, is_booster=True)]),
            Pymon('Splant', FighterType.PLANT, 25, [Hability('Hoja navaja', 3,5,2,5,7,4), Hability('Mordisco', 2,2,2,2,2,2), Hability('Cabezazo',2,2,2,2,2,2), Hability('Rayo solar', 0,0,0,0,0,0, turns_delay=3, booster_last=2, is_booster=True)]),
            Pymon('Rockdog', FighterType.ROCK, 25, [Hability('Roca afilado', 3,5,2,5,7,4), Hability('Velocidad', 2,2,2,2,2,2), Hability('Cola ferrea', 2,2,2,2,2,2), Hability('Campo rocoso', 0,0,0,0,0,0, turns_delay=3, booster_last=2, is_booster=True)])
        ]


