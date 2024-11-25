# src/states/title_state.py

import pygame as pg
from ..settings import SCREEN_WIDTH, SCREEN_HEIGHT

class TitleState:
    def __init__(self, state_machine, assets):
        self.state_machine = state_machine
        self.assets = assets
        self.font = self.assets.get_font(72)
        self.title_text = self.font.render('BIPPY', True, (236, 180, 28))
        self.play_button_rect = pg.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2, 200, 50)

    def update(self, dt, events):
        for event in events:
            if event.type == pg.MOUSEBUTTONDOWN:
                if self.play_button_rect.collidepoint(event.pos):
                    from .playing_state import PlayingState
                    self.state_machine.add_state('playing', PlayingState(self.state_machine, self.assets))
                    self.state_machine.change_state('playing')

    def draw(self, surface):
        surface.fill((0, 0, 0))
        surface.blit(
            self.title_text,
            (SCREEN_WIDTH // 2 - self.title_text.get_width() // 2, 100)
        )
        pg.draw.rect(surface, (255, 255, 255), self.play_button_rect)
        play_text = self.font.render('PLAY', True, (0, 0, 0))
        surface.blit(
            play_text,
            (
                self.play_button_rect.centerx - play_text.get_width() // 2,
                self.play_button_rect.centery - play_text.get_height() // 2
            )
        )