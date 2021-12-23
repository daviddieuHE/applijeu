from src.gameplay import Gameplay
from src.player import Player

if __name__ == '__main__':
    try:
        gp = Gameplay(Player.creat_player())

        while True:
            gp.interaction(gp.ask_combat())
    except Exception as e:
        print(str(e))
