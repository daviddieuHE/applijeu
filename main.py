from mobs.mobs import Mobs
from gameplay import gameplay
from player import player


if __name__ == '__main__':
    Mobs.creatMobs()
    gameplay.interaction()
    gameplay.fight()
    gameplay.creatPlayer()
