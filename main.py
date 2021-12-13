from mobs.mobs import Mobs
from gameplay import gameplay


if __name__ == '__main__':
    Mobs.creatMobs()
    gameplay.interaction()
    gameplay.fight()