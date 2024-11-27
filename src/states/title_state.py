# src/states/title_state.py

import pygame as pg
from ..assets import AssetManager
from .state_machine import StateMachine
from ..settings import SCREEN_WIDTH, SCREEN_HEIGHT
from ..utils.helpers import tint_image
import math

class TitleState:
    def __init__(self, state_machine, assets):
        self.state_machine = state_machine
        self.assets = assets
        self.font = self.assets.get_font(48)  # Button font
        self.title_font = self.assets.get_font(144)  # Title font (adjusted size)

        # Render title text
        self.title_text = self.title_font.render('BIPPY', True, (80, 200, 120))  # Emerald Green
        self.title_shadow = self.title_font.render('BIPPY', True, (34, 34, 34))  # Shadow Color
        self.title_shadow_offset = (5, 5)

        # Play button setup
        rust_orange = (183, 65, 14)
        goldenrod = (218, 165, 32)
        # If you prefer tinting, uncomment the following lines
        # self.play_button_image = tint_image(self.assets.get_image('play_button'), rust_orange)
        # self.play_button_hover_image = tint_image(self.assets.get_image('play_button_hover'), goldenrod)
        self.play_button_image = self.assets.get_image('play_button')
        self.play_button_hover_image = self.assets.get_image('play_button_hover')
        self.play_button_rect = self.play_button_image.get_rect(
            center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100)
        )
        print(f"Play Button Rect Initialized at: {self.play_button_rect.center}")

        # Decorative elements
        self.tree_color = (80, 200, 120)  # Emerald Green
        self.tree_positions = [
            (100, SCREEN_HEIGHT - 150),
            (SCREEN_WIDTH - 100, SCREEN_HEIGHT - 150)
        ]

        # Character silhouette (if available)
        if self.assets.get_image('bippy_silhouette'):
            self.bippy_silhouette = self.assets.get_image('bippy_silhouette')
            self.bippy_rect = self.bippy_silhouette.get_rect(
                center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 150)
            )
        else:
            self.bippy_silhouette = None

        # Button state
        self.is_hovering_play = False

        # Optional: Background Music Setup
        # Uncomment if you have background music
        """
        pg.mixer.music.load(self.assets.get_sound('background_music'))
        pg.mixer.music.set_volume(0.5)
        pg.mixer.music.play(-1)  # Loop indefinitely
        """

    def update(self, dt, events):
        mouse_pos = pg.mouse.get_pos()
        self.is_hovering_play = self.play_button_rect.collidepoint(mouse_pos)

        for event in events:
            if event.type == pg.MOUSEBUTTONDOWN:
                if self.is_hovering_play:
                    # Optional: Play click sound
                    # self.assets.get_sound('button_click').play()

                    from .playing_state import PlayingState
                    self.state_machine.add_state('playing', PlayingState(self.state_machine, self.assets))
                    self.state_machine.change_state('playing')

    def draw(self, surface):
        # Fill background with Dark Olive Green
        surface.fill((85, 107, 47))  # Dark Olive Green

        # Draw decorative trees
        for pos in self.tree_positions:
            # Draw trunk
            pg.draw.rect(surface, (101, 67, 33), (pos[0] - 5, pos[1], 10, 50))  # Brown trunk
            # Draw foliage (triangle)
            pg.draw.polygon(surface, self.tree_color, [
                (pos[0], pos[1] - 40),
                (pos[0] - 30, pos[1]),
                (pos[0] + 30, pos[1])
            ])

        # Draw ground (optional simple pattern)
        for x in range(0, SCREEN_WIDTH, 100):
            pg.draw.line(surface, (34, 139, 34), (x, SCREEN_HEIGHT - 50), (x + 50, SCREEN_HEIGHT - 50), 2)

        # Draw character silhouette if available
        if self.bippy_silhouette:
            surface.blit(self.bippy_silhouette, self.bippy_rect)

        # Draw title shadow
        surface.blit(
            self.title_shadow,
            (
                SCREEN_WIDTH // 2 - self.title_shadow.get_width() // 2 + self.title_shadow_offset[0],
                100 + self.title_shadow_offset[1]
            )
        )

        # Draw main title text
        surface.blit(
            self.title_text,
            (SCREEN_WIDTH // 2 - self.title_text.get_width() // 2, 100)
        )

        # Draw Play Button with hover effect
        if self.is_hovering_play:
            surface.blit(self.play_button_hover_image, self.play_button_rect)
            play_text_y = (self.play_button_rect.centery + 4 - (self.font.size('PLAY')[1] // 2)) - 5  # Shift down by 6 pixels
        else:
            surface.blit(self.play_button_image, self.play_button_rect)
            play_text_y = (self.play_button_rect.centery - (self.font.size('PLAY')[1] // 2)) - 5  # Centered

        # Draw Play Button Text
        play_text = self.font.render('PLAY', True, (255, 255, 255))  # White text
        surface.blit(
            play_text,
            (
                self.play_button_rect.centerx - play_text.get_width() // 2,
                play_text_y
            )
        )

if __name__ == '__main__':
    pg.init()
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pg.display.set_caption('title state test env')
    clock = pg.time.Clock()
    state_machine = StateMachine()
    assets = AssetManager()
    state_machine.add_state('title', TitleState(state_machine, assets))
    state_machine.change_state('title')
    running = True
    while running:
        dt = clock.tick(60) / 1000
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                running = False
        state_machine.update(dt, events)
        state_machine.draw(screen)
        pg.display.flip()
    pg.quit()