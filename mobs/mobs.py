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
