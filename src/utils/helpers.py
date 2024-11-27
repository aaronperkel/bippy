# src/utils/helpers.py

import pygame as pg

def clamp(value, min_value, max_value):
    return max(min_value, min(value, max_value))

def tint_image(image, tint_color):
    """Apply a tint to an image."""
    tinted_image = image.copy()
    tinted_image.fill(tint_color + (0,), None, pg.BLEND_RGBA_MULT)
    return tinted_image