# tests/test_obstacle.py
import unittest
import pygame as pg
from src.entities.obstacle import Obstacle
from src.assets import AssetManager

class TestObstacle(unittest.TestCase):
    def setUp(self):
        pg.init()
        self.assets = AssetManager()
        self.obstacle = Obstacle(500, self.assets)

    def test_initial_position(self):
        self.assertEqual(self.obstacle.rect.x, 500)

    def test_movement(self):
        initial_x = self.obstacle.rect.x
        self.obstacle.update(0.016)
        self.assertLess(self.obstacle.rect.x, initial_x)

if __name__ == '__main__':
    unittest.main()