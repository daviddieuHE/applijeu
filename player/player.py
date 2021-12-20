import mobs

class Player:

    xp = 0

    def __init__(self, pseudo, lvl, xp, pv, pa):
        assert len(pseudo) in range(3, 16), "Attribut 'pseudo' : le pseudo peut avoir entre 3 et 15 lettres"
        self.pseudo = pseudo
        self.lvl = lvl
        self.xp = xp
        self.pv = pv
        self.pa = pa

    def __str__(self):
        return f"[pseudo : {self.pseudo} / lvl : {self.lvl}, xp : {self.xp}, pv : {self.pv}, pa : {self.pa}]"

    def lvl_up(self, xp):
        if xp >= 50:
            self.lvl += 1
            self.pv += 50
            self.pa += 15

    def fight_mob(self, mob):
        randomMobs()
        print("{} attaque {}\n"
              "{} perds {} pv".format(Mobs.mobs_dic[i].name, Player.pseudo))
        print("il reste {} pv à {} et {} pv à {}".format(Mobs.mobs_dic[i].pv, Mobs.mobs_dic[i].name, ))
