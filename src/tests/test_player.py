# tests/test_player.py
import unittest
import pygame as pg
from src.entities.player import Player
from src.assets import AssetManager

class TestPlayer(unittest.TestCase):
    def setUp(self):
        pg.init()
        self.assets = AssetManager()
        self.player = Player(100, 100, self.assets)

    def test_initial_position(self):
        self.assertEqual(self.player.rect.topleft, (100, 100))

    def test_jump(self):
        self.player.is_jumping = False
        self.player.vel_y = 0
        keys = {pg.K_SPACE: True}
        self.player.update(0, keys)
        self.assertTrue(self.player.is_jumping)
        self.assertEqual(self.player.vel_y, -18)

if __name__ == '__main__':
    unittest.main()