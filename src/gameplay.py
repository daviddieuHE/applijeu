import random
import time
from copy import copy
from src.mobs import Mobs


class Gameplay:

    def __init__(self, player):
        self.player = player
        self.mob = None
        self.mobs = {}

        self.mobs[0] = Mobs("ogre", 1, 30, 10)
        self.mobs[1] = Mobs("ogre", 2, 60, 20)
        self.mobs[2] = Mobs("ogre", 3, 90, 30)
        self.mobs[3] = Mobs("witch", 1, 30, 10)
        self.mobs[4] = Mobs("dragon", 5, 300, 50)

        if player is None:
            raise ValueError("player n'est pas défini")

    def ask_combat(self):
        self.mob = copy(self.mobs[random.randrange(0, len(self.mobs))])
        return input(f"vous vous apprêté à combatre un {self.mob.name} de niveau {self.mob.lvl} ayant {self.mob.pv} pv et {self.mob.pa} pa\nacceptez vous le combat ? ")

    def interaction(self, answer):
        if answer.lower() in ("yes", "oui", "y", "o"):
            while not (self.player.pv <= 0 or self.mob.pv <= 0):
                self.player.fight_mob(self.mob)
                self.mob.fight_player(self.player)
            time.sleep(1)
            if self.player.pv > self.mob.pv:
                self.player.xp += 15
                self.player.pv = 100
                print(f"{self.player.pseudo} a gagné")
                print(f"xp: {self.player.xp}")
            else:
                print("looser")