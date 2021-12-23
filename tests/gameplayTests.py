import unittest
from src.gameplay import Gameplay
from src.mobs import Mobs
from src.player import Player


class gameplayTests(unittest.TestCase):

    def test_init(self):
        gp = Gameplay(Player("Koba"))
        self.assertGreater(len(gp.mobs), 2, "Gameplay doit avoir au moins 3 mobs")

    def test_player_not_none(self):
        self.assertRaises(ValueError, Gameplay, None)

    def test_accept_combat(self):
        for accept_str in ("yes", "oui", "y", "o"):
            gp = Gameplay(Player("Koba"))
            gp.mob = Mobs("testmob", 1, 1, 0)
            gp.interaction(accept_str)
            self.assertTrue(gp.player.xp > 0 and gp.mob.pv <= 0,
                         "Le combat doit avoir lieu si le joueur l'accepte")

    def test_refuse_combat(self):
        for accept_str in ("non", "no", "n"):
            gp = Gameplay(Player("Koba"))
            gp.mob = Mobs("testmob", 1, 1, 0)
            gp.interaction(accept_str)
            self.assertTrue(gp.player.xp == 0 and gp.mob.pv > 0,
                         "Le combat ne doit pas avoir lieu si le joueur le refuse")
