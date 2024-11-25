# src/settings.py
import os

# Screen settings
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
FPS = 60
TITLE = 'Bippy Game'

# Base directory (adjust as needed)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Asset directories
ASSETS_DIR = os.path.join(BASE_DIR, 'assets')
IMAGE_DIR = os.path.join(ASSETS_DIR, 'images')
SOUND_DIR = os.path.join(ASSETS_DIR, 'sounds')
FONT_DIR = os.path.join(ASSETS_DIR, 'fonts')