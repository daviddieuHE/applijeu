class Player:

    xp = 0

    def __init__(self, pseudo='default', classe='default', lvl='default', xp='default', pv='default', pa ='default'):
        self.pseudo = "koba"
        self.classe = "ranger"
        self.lvl = 1
        self.xp = 0
        self.pv = 100
        self.pa = 15


    def lvl_up(self, xp):
        if xp >= 50:
            self.lvl += 1
            self.pv += 50
            self.pa += 15
