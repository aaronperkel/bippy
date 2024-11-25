# src/assets.py
import pygame as pg
import os
from .settings import IMAGE_DIR, SOUND_DIR, FONT_DIR

class AssetManager:
    def __init__(self):
        self.images = {}
        self.sounds = {}
        self.fonts = {}
        self.load_assets()
    
    def load_assets(self):
        # Load images
        self.images['button'] = pg.image.load(os.path.join(IMAGE_DIR, 'button.png')).convert_alpha()
        self.images['buttonPress'] = pg.image.load(os.path.join(IMAGE_DIR, 'buttonPress.png')).convert_alpha()
        # Scale images proportionally
        self.images['man'] = pg.transform.scale(pg.image.load(os.path.join(IMAGE_DIR, 'man.png')).convert_alpha(), (100, 92))
        self.images['manSad'] = pg.transform.scale(pg.image.load(os.path.join(IMAGE_DIR, 'manSad.png')).convert_alpha(), (256, 256))
        # Load other images similarly...

        # Load fire images
        self.images['fire'] = [
            pg.transform.scale(pg.image.load(os.path.join(IMAGE_DIR, 'fire1.png')).convert_alpha(), (84, 100)),
            pg.transform.scale(pg.image.load(os.path.join(IMAGE_DIR, 'fire2.png')).convert_alpha(), (90, 100)),
            pg.transform.scale(pg.image.load(os.path.join(IMAGE_DIR, 'fire3.png')).convert_alpha(), (90, 100)),
        ]
        self.images['pipe'] = pg.transform.scale(pg.image.load(os.path.join(IMAGE_DIR, 'pipe.png')).convert_alpha(), (96, 192))

        # Load fonts
        self.fonts['large'] = os.path.join(FONT_DIR, 'font.ttf')
        self.fonts['medium'] = os.path.join(FONT_DIR, 'font.ttf')
        self.fonts['small'] = os.path.join(FONT_DIR, 'font.ttf')

        # Pre-render texts
        self.pre_render_texts()

    def pre_render_texts(self):
        # Create font objects
        font_large = pg.font.Font(self.fonts['large'], 228)
        font_medium = pg.font.Font(self.fonts['medium'], 48)
        font_small = pg.font.Font(self.fonts['small'], 36)
        
        # Render texts
        self.images['play_text'] = font_medium.render('PLAY!', True, (0, 0, 0))
        self.images['controls_text'] = font_medium.render('CONTROLS', True, (0, 0, 0))
        self.images['title_text'] = font_large.render('BIPPY', True, (236, 180, 28))
        # Continue rendering other texts...

    def get_image(self, key):
        return self.images.get(key)
    
    def get_font(self, size):
        return pg.font.Font(self.fonts['medium'], size)