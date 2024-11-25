# src/states/playing_state.py
import pygame as pg
import random
from ..entities.player import Player
from ..entities.obstacle import Obstacle
from ..settings import SCREEN_WIDTH, SCREEN_HEIGHT
from .game_over_state import GameOverState

class PlayingState:
    def __init__(self, state_machine, assets):
        self.state_machine = state_machine
        self.assets = assets
        player_start_x = SCREEN_WIDTH * 0.1
        player_start_y = SCREEN_HEIGHT - 48 - self.assets.get_image('man').get_height()
        self.player = Player(player_start_x, player_start_y, self.assets)
        self.obstacles = pg.sprite.Group()
        self.bg_x = 0
        self.bg_speed = 6
        self.score = 0
        self.last_obstacle_time = pg.time.get_ticks()
        self.obstacle_interval = 1000
        self.start_time = pg.time.get_ticks()

    def update(self, dt, events):
        keys_pressed = pg.key.get_pressed()
        self.player.update(keys_pressed)
        self.bg_x -= self.bg_speed
        bg_width = self.assets.get_image('bg1').get_width()
        if self.bg_x <= -bg_width:
            self.bg_x = 0
        current_time = pg.time.get_ticks()
        if current_time - self.last_obstacle_time > self.obstacle_interval:
            obstacle_x = SCREEN_WIDTH + random.randint(0, 200)
            obstacle = Obstacle(obstacle_x, self.bg_speed, self.assets)
            self.obstacles.add(obstacle)
            self.last_obstacle_time = current_time
        self.obstacles.update()
        if pg.sprite.spritecollideany(self.player, self.obstacles):
            self.state_machine.add_state('game_over', GameOverState(self.state_machine, self.assets, self.score))
            self.state_machine.change_state('game_over')
        self.score += 1

    def draw(self, surface):
        bg1 = self.assets.get_image('bg1')
        surface.blit(bg1, (self.bg_x, 0))
        surface.blit(bg1, (self.bg_x + bg1.get_width(), 0))
        surface.blit(self.player.image, self.player.rect)
        for obstacle in self.obstacles:
            obstacle.draw(surface)
        score_text = self.assets.get_font(48).render(str(self.score), True, (0, 0, 0))
        surface.blit(score_text, (20, 20))