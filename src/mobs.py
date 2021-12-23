import time

class Mobs:

    def __init__(self, name, lvl, pv, pa):
        self.name = name
        self.lvl = lvl
        self.pv = pv
        self.pa = pa


    def fight_player(self, player):
        if self.pv > 0:
            player.pv -= self.pa
            print(f"{self.name} attaque {player.pseudo}, {player.pseudo} perds {self.pa} pv\n")
            time.sleep(1)
            print(f"il reste {self.pv} pv à {self.name} et {player.pv} pv à {player.pseudo}\n")
            time.sleep(1)