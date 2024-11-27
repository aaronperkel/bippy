# src/assets.py

import pygame as pg
import os
from .settings import IMAGE_DIR, SOUND_DIR, FONT_DIR, SCREEN_WIDTH, SCREEN_HEIGHT

class AssetManager:
    def __init__(self):
        self.images = {}
        self.sounds = {}
        self.fonts = {}
        self.load_assets()
    
    def load_assets(self):
        # Load images
        self.images['play_button'] = pg.image.load(os.path.join(IMAGE_DIR, 'ui/play_button.png')).convert_alpha()
        self.images['play_button_hover'] = pg.image.load(os.path.join(IMAGE_DIR, 'ui/play_button_hover.png')).convert_alpha()
        
        # Scale images proportionally
        self.images['man'] = pg.transform.scale(
            pg.image.load(os.path.join(IMAGE_DIR, 'characters/bippy/man.png')).convert_alpha(), (100, 92))
        self.images['manSad'] = pg.transform.scale(
            pg.image.load(os.path.join(IMAGE_DIR, 'characters/bippy/manSad.png')).convert_alpha(), (256, 256))
        self.images['bg'] = pg.transform.scale(
            pg.image.load(os.path.join(IMAGE_DIR, 'backgrounds/bg.png')).convert_alpha(), (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.images['girl'] = pg.transform.scale(
            pg.image.load(os.path.join(IMAGE_DIR, 'characters/girl.png')).convert_alpha(), (108, 92))
        self.images['villain'] = pg.transform.scale(
            pg.image.load(os.path.join(IMAGE_DIR, 'characters/villain.png')).convert_alpha(), (82, 120))
        self.images['bg1'] = pg.transform.scale(
            pg.image.load(os.path.join(IMAGE_DIR, 'backgrounds/bg1.png')).convert_alpha(), (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.images['space'] = pg.transform.scale(
            pg.image.load(os.path.join(IMAGE_DIR, 'ui/space.png')).convert_alpha(), (800, 200))
        self.images['spacePress'] = pg.transform.scale(
            pg.image.load(os.path.join(IMAGE_DIR, 'ui/spacePress.png')).convert_alpha(), (800, 200))
        self.images['keyboard'] = pg.transform.scale(
            pg.image.load(os.path.join(IMAGE_DIR, 'ui/keyboard.png')).convert_alpha(), (590, 200))
        self.images['upPress'] = pg.transform.scale(
            pg.image.load(os.path.join(IMAGE_DIR, 'ui/upPress.png')).convert_alpha(), (196, 98))
        self.images['leftPress'] = pg.transform.scale(
            pg.image.load(os.path.join(IMAGE_DIR, 'ui/leftPress.png')).convert_alpha(), (190, 200))
        self.images['rightPress'] = pg.transform.scale(
            pg.image.load(os.path.join(IMAGE_DIR, 'ui/rightPress.png')).convert_alpha(), (190, 200))
        
        # Load fire images
        self.images['fire'] = [
            pg.transform.scale(
                pg.image.load(os.path.join(IMAGE_DIR, 'obstacles/fire1.png')).convert_alpha(), (84, 100)),
            pg.transform.scale(
                pg.image.load(os.path.join(IMAGE_DIR, 'obstacles/fire2.png')).convert_alpha(), (90, 100)),
            pg.transform.scale(
                pg.image.load(os.path.join(IMAGE_DIR, 'obstacles/fire3.png')).convert_alpha(), (90, 100)),
        ]
        self.images['pipe'] = pg.transform.scale(
            pg.image.load(os.path.join(IMAGE_DIR, 'obstacles/pipe.png')).convert_alpha(), (96, 192))
        
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
        self.images['go_text'] = font_large.render('SAVE FIPPY!', True, (236, 180, 28))
        self.images['end_text'] = font_large.render('GAME OVER', True, (236, 180, 28))
        self.images['jump_text'] = font_medium.render('JUMP - space bar or up arrow', True, (0, 0, 0))
        self.images['move_text'] = font_medium.render('MOVE - left or right arrow', True, (0, 0, 0))
        self.images['back_text'] = font_small.render('BACK', True, (0, 0, 0))
        self.images['restart_text'] = font_medium.render('RESTART', True, (0, 0, 0))
        # Dialogue Texts
        self.images['fippy1_text'] = font_medium.render('Hey Bippy <3', True, (0, 0, 0))
        self.images['fippy2_text'] = font_medium.render('AHHH! HELP!', True, (0, 0, 0))
        self.images['bippy1_text'] = font_medium.render('Hey Fippy <3', True, (0, 0, 0))
        self.images['bippy2_text'] = font_medium.render('FIPPY WATCH OUT!', True, (0, 0, 0))
        self.images['bippy3_text'] = font_medium.render('I\'LL SAVE YOU!', True, (0, 0, 0))
        self.images['villain1_text'] = font_medium.render('I got you now Fippy!', True, (0, 0, 0))
    
    def get_image(self, key):
        return self.images.get(key)
    
    def get_font(self, size):
        return pg.font.Font(self.fonts['medium'], size)