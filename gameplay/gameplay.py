from mobs.mobs import Mobs
from player.player import Player
import random



def randomMob():
    i = random.randrange(0, 4)
    return i

def interaction():
    i = randomMob()
    print("vous vous apprêté à combatre un {} de niveau {} ayant {} pv et {} pa".format(Mobs.mobs_dic[i].name,Mobs.mobs_dic[i].lvl,Mobs.mobs_dic[i].pv, Mobs.mobs_dic[i].pa))
    #askfight = input("acceptez vous le combat ? ")

def fight():
    i = randomMob()
    pvMobTemp = Mobs.mobs_dic[i].pv
    paMobTemp = Mobs.mobs_dic[i].pa

    pvPlayerTemp = Player.__init__(self).pv
    paPlayerTemp = Player.__init__(self).pa

    print(pvMobTemp, paMobTemp)
    print(pvPlayerTemp, paPlayerTemp)

