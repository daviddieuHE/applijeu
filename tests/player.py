import unittest

from src.player import Player


class PlayerTest(unittest.TestCase):

    def test_pseudo_length(self):
        # test 2 < player pseudo length < 17
        self.assertRaises(ValueError, Player, "as")
        self.assertRaises(ValueError, Player, "fisjebasfgdfdyhdy")

    def test_pseudo_valid(self):
        self.assertEqual(Player("abcd").pseudo, "abcd")

    def test_pseudo_is_ascii(self):
        # test if player pseudo is all ascii
        self.assertRaises(ValueError, Player, "大大大大")

    def test_pseudo_is_alpha(self):
        self.assertRaises(ValueError, Player, "12%%##//")

    def test_player_default_values(self):
        # test player lvl, xp, pvp and pa initialized at the right values
        self.assertEqual(Player("validpseudo").lvl, 1)
        self.assertEqual(Player("validpseudo").xp, 0)
        self.assertEqual(Player("validpseudo").pv, 100)
        self.assertEqual(Player("validpseudo").pa, 15)

