# src/entities/obstacle.py
import pygame as pg
from settings import SCREEN_HEIGHT

class Obstacle(pg.sprite.Sprite):
    def __init__(self, x, assets):
        super().__init__()
        self.assets = assets
        self.images = [
            self.assets.get_image('fire1'),
            self.assets.get_image('fire2'),
            self.assets.get_image('fire3'),
        ]
        self.current_image = 0
        self.rect = self.images[0].get_rect(midbottom=(x, SCREEN_HEIGHT - 50))
        self.animation_timer = 0

    def update(self, dt):
        self.rect.x -= 5  # Move obstacle to the left
        if self.rect.right < 0:
            self.kill()

        # Handle animation
        self.animation_timer += dt
        if self.animation_timer >= 0.2:  # Change frame every 0.2 seconds
            self.animation_timer = 0
            self.current_image = (self.current_image + 1) % len(self.images)

    def draw(self, surface):
        surface.blit(self.images[self.current_image], self.rect)