from zerg_rush import ZergRushBot

import sc2
from sc2 import Race
from sc2.player import Human, Bot


def main():
    sc2.run_game(sc2.maps.get("Abyssal Reef LE"), [
        Human(Race.Terran),
        Bot(Race.Zerg, ZergRushBot())
    ], realtime=True)

if __name__ == '__main__':
    main()
