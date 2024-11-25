# src/entities/player.py
import pygame as pg
from settings import GRAVITY, JUMP_VELOCITY

class Player(pg.sprite.Sprite):
    def __init__(self, x, y, assets):
        super().__init__()
        self.assets = assets
        self.image = self.assets.get_image('bippy_idle')
        self.rect = self.image.get_rect(topleft=(x, y))
        self.vel_y = 0
        self.is_jumping = False

    def update(self, dt, events):
        keys = pg.key.get_pressed()
        if not self.is_jumping:
            if keys[pg.K_SPACE] or keys[pg.K_UP]:
                self.is_jumping = True
                self.vel_y = JUMP_VELOCITY

        if self.is_jumping:
            self.vel_y += GRAVITY
            self.rect.y += self.vel_y
            if self.rect.bottom >= 800 - 50:  # Assuming ground level
                self.rect.bottom = 800 - 50
                self.is_jumping = False
                self.vel_y = 0

        if keys[pg.K_LEFT]:
            self.rect.x -= 5
        if keys[pg.K_RIGHT]:
            self.rect.x += 5

    def draw(self, surface):
        surface.blit(self.image, self.rect)