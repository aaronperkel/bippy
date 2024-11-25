# src/entities/obstacle.py
import pygame as pg
from ..settings import SCREEN_HEIGHT

class Obstacle(pg.sprite.Sprite):
    def __init__(self, x, speed, assets):
        super().__init__()
        self.images = assets.get_image('fire')  # List of fire images
        self.current_image = 0
        self.animation_speed = 0.15
        self.animation_timer = 0
        self.rect = self.images[0].get_rect(midbottom=(x, SCREEN_HEIGHT - 48))
        self.speed = speed
        self.pipe_image = assets.get_image('pipe')

    def update(self):
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.kill()
        self.animation_timer += self.animation_speed
        if self.animation_timer >= 1:
            self.animation_timer = 0
            self.current_image = (self.current_image + 1) % len(self.images)

    def draw(self, surface):
        image = self.images[self.current_image]
        surface.blit(image, self.rect)
        pipe_rect = self.pipe_image.get_rect(midtop=(self.rect.centerx, self.rect.bottom))
        surface.blit(self.pipe_image, pipe_rect)