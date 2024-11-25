# src/entities/player.py
import pygame as pg
from ..settings import SCREEN_WIDTH, SCREEN_HEIGHT

class Player(pg.sprite.Sprite):
    def __init__(self, x, y, assets):
        super().__init__()
        self.image = assets.get_image('man')
        self.rect = self.image.get_rect(topleft=(x, y))
        self.vel_y = 0
        self.is_jumping = False
        self.assets = assets

    def update(self, keys_pressed):
        if not self.is_jumping:
            if keys_pressed[pg.K_SPACE] or keys_pressed[pg.K_UP]:
                self.is_jumping = True
                self.vel_y = -18
        if self.is_jumping:
            self.vel_y += 0.6  # Gravity
            self.rect.y += self.vel_y
            if self.rect.bottom >= SCREEN_HEIGHT - 48:
                self.rect.bottom = SCREEN_HEIGHT - 48
                self.is_jumping = False
                self.vel_y = 0
        if keys_pressed[pg.K_LEFT]:
            self.rect.x -= 7
            if self.rect.left < 0:
                self.rect.left = 0
        if keys_pressed[pg.K_RIGHT]:
            self.rect.x += 7
            if self.rect.right > SCREEN_WIDTH:
                self.rect.right = SCREEN_WIDTH