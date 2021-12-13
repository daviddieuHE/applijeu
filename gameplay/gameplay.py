from mobs.mobs import Mobs
from player.player import Player
import random


def creatPlayer():
    p1 = Player("koba", 1, 0, 100, 15)

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

    print(pvMobTemp, paMobTemp)


    Player.xp += 10
