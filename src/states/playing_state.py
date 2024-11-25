# src/states/playing_state.py
import pygame as pg
from settings import SCREEN_WIDTH, SCREEN_HEIGHT
from entities.player import Player
from entities.obstacle import Obstacle
import random

class PlayingState:
    def __init__(self, state_machine, assets):
        self.state_machine = state_machine
        self.assets = assets
        self.player = Player(100, SCREEN_HEIGHT - 150, self.assets)
        self.obstacles = pg.sprite.Group()
        self.last_obstacle_time = pg.time.get_ticks()
        self.obstacle_interval = 1000  # milliseconds

    def update(self, dt, events):
        self.player.update(dt, events)

        # Spawn Obstacles
        current_time = pg.time.get_ticks()
        if current_time - self.last_obstacle_time > self.obstacle_interval:
            obstacle = Obstacle(SCREEN_WIDTH + 100, self.assets)
            self.obstacles.add(obstacle)
            self.last_obstacle_time = current_time

        # Update Obstacles
        self.obstacles.update(dt)

        # Check for collisions
        if pg.sprite.spritecollideany(self.player, self.obstacles):
            from states.game_over_state import GameOverState
            self.state_machine.add_state('game_over', GameOverState(self.state_machine, self.assets))
            self.state_machine.change_state('game_over')

    def draw(self, surface):
        surface.fill((135, 206, 235))  # Sky blue background
        self.player.draw(surface)
        for obstacle in self.obstacles:
            obstacle.draw(surface)