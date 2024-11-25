# src/assets.py
import pygame as pg
import os
from settings import IMAGE_DIR, SOUND_DIR, FONT_DIR

class AssetManager:
    def __init__(self):
        self.images = {}
        self.sounds = {}
        self.fonts = {}
        self.load_assets()

    def load_assets(self):
        # Load images
        self.images['bippy_idle'] = pg.image.load(os.path.join(IMAGE_DIR, 'characters', 'bippy', 'idle.png')).convert_alpha()
        self.images['bippy_run'] = pg.image.load(os.path.join(IMAGE_DIR, 'characters', 'bippy', 'run.png')).convert_alpha()
        self.images['bippy_jump'] = pg.image.load(os.path.join(IMAGE_DIR, 'characters', 'bippy', 'jump.png')).convert_alpha()
        # Load other images similarly

        # Load sounds
        # self.sounds['jump'] = pg.mixer.Sound(os.path.join(SOUND_DIR, 'jump.wav'))
        # self.sounds['collision'] = pg.mixer.Sound(os.path.join(SOUND_DIR, 'collision.wav'))
        # Load music
        # pg.mixer.music.load(os.path.join(SOUND_DIR, 'music.mp3'))

        # Load fonts
        self.fonts['large'] = os.path.join(FONT_DIR, 'font.ttf')
        self.fonts['medium'] = os.path.join(FONT_DIR, 'font.ttf')
        self.fonts['small'] = os.path.join(FONT_DIR, 'font.ttf')

    def get_image(self, key):
        return self.images.get(key)

    def get_sound(self, key):
        return self.sounds.get(key)

    def get_font(self, size):
        return pg.font.Font(self.fonts['medium'], size)