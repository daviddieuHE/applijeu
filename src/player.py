import time

class Player:

    def __init__(self, pseudo):
        # assert len(pseudo) in range(3, 16), "Attribut 'pseudo' : le pseudo peut avoir entre 3 et 15 lettres"
        self.pseudo = pseudo
        self.lvl = 1
        self._xp = 0
        self.pv = 100
        self.pa = 15

        if not 2 < len(pseudo) < 17:
            raise ValueError("pseudo doit avoir entre 3 et 17 caractère")
        if not pseudo.isascii():
            raise ValueError("parle français cousin")
        if not pseudo.isalpha():
            raise ValueError("utilisez uniquament des lettres")


    @property
    def xp(self):
        return self._xp

    @xp.setter
    def xp(self, value):
        if self.lvl * 50 < value:
            self.lvl_up()
        self._xp = value

    @staticmethod
    def creat_player():
        return Player(input("choisissez votre pseudo : "))

    def __str__(self):
        return f"[pseudo : {self.pseudo} / lvl : {self.lvl}, xp : {self.xp}, pv : {self.pv}, pa : {self.pa}]"

    def lvl_up(self):
        self.lvl += 1
        self.pv += 50
        self.pa += 15
        print(
            "Level up !\n"
            f"lvl: {self.lvl}\n"
            f"pv: {self.pv}\n"
            f"pa: {self.pa}"
        )

    def fight_mob(self, mob):
        if self.pv > 0:
            mob.pv -= self.pa
            print(f"{self.pseudo} attaque {mob.name}, {mob.name} perds {self.pa} pv\n")
            time.sleep(1)
            print(f"il reste {mob.pv} pv à {mob.name} et {self.pv} pv à {self.pseudo}\n")
            time.sleep(1)