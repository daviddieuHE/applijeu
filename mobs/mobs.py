import player
import mobs
class Mobs:

    mobs_dic = {}

    def __init__(self, name, lvl, pv, pa):
        self.name = name
        self.lvl = lvl
        self.pv = pv
        self.pa = pa


    def creatMobs():
        Mobs.mobs_dic[0] = Mobs("ogre", 1, 30, 10)
        Mobs.mobs_dic[1] = Mobs("ogre", 2, 60, 20)
        Mobs.mobs_dic[2] = Mobs("ogre", 3, 90, 30)
        Mobs.mobs_dic[3] = Mobs("witch", 1, 30, 10)
        Mobs.mobs_dic[4] = Mobs("dragon", 5, 300, 50)

    def randomMob(self):
        i = random.randrange(0, 4)
        return i

    def interaction():
        i = randomMob()
        print("vous vous apprêté à combatre un {} de niveau {} ayant {} pv et {} pa".format(Mobs.mobs_dic[i].name,
                                                                                            Mobs.mobs_dic[i].lvl,
                                                                                            Mobs.mobs_dic[i].pv,
                                                                                            Mobs.mobs_dic[i].pa))
    def fight_player(self, player):
        randomMobs()
        print("{} attaque {}\n"
              "{} perds {} pv".format(Mobs.mobs_dic[i].name, Player.pseudo))
        print("il reste {} pv à {} et {} pv à {}".format(Mobs.mobs_dic[i].pv, Mobs.mobs_dic[i].name, ))

    def  une fonction(ceci est un easter egg)