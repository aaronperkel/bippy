# src/states/game_over_state.py

import pygame as pg
from ..settings import SCREEN_WIDTH, SCREEN_HEIGHT

class GameOverState:
    def __init__(self, state_machine, assets, score):
        self.state_machine = state_machine
        self.assets = assets
        self.score = score  # Store the score
        self.font = self.assets.get_font(72)
        self.game_over_text = self.font.render('GAME OVER', True, (236, 28, 36))
        self.restart_button_rect = pg.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2, 200, 50)

    def update(self, dt, events):
        for event in events:
            if event.type == pg.MOUSEBUTTONDOWN:
                if self.restart_button_rect.collidepoint(event.pos):
                    from .playing_state import PlayingState
                    self.state_machine.add_state('playing', PlayingState(self.state_machine, self.assets))
                    self.state_machine.change_state('playing')

    def draw(self, surface):
        surface.fill((0, 0, 0))
        # Display Game Over Text
        surface.blit(
            self.game_over_text,
            (SCREEN_WIDTH // 2 - self.game_over_text.get_width() // 2, 100)
        )
        # Display Score
        score_text = self.assets.get_font(48).render(f'Your Score: {self.score}', True, (255, 255, 255))
        surface.blit(
            score_text,
            (SCREEN_WIDTH // 2 - score_text.get_width() // 2, 200)
        )
        # Draw Restart Button
        pg.draw.rect(surface, (255, 255, 255), self.restart_button_rect)
        restart_text = self.font.render('RESTART', True, (0, 0, 0))
        surface.blit(
            restart_text,
            (
                self.restart_button_rect.centerx - restart_text.get_width() // 2,
                self.restart_button_rect.centery - restart_text.get_height() // 2
            )
        )