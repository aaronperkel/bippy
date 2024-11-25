"""
Bippy Game

A side-scrolling platformer where you control Bippy on a mission to save Fippy from the villain.
Jump over obstacles and avoid hazards to reach your goal.

Author: Aaron Perkel
Date: November 2024
"""

import pygame as pg
import sys
import random

# Constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
FPS = 60

# Initialize Pygame
pg.init()
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption('Bippy')
clock = pg.time.Clock()

# Game States
TITLE = 'title'
CONTROLS = 'controls'
INTRO = 'intro'
PLAYING = 'playing'
GAME_OVER = 'game_over'

# Assets Loading Function
def load_assets():
    assets = {}
    # Load images
    assets['button'] = pg.image.load('textures/button.png')
    assets['buttonPress'] = pg.image.load('textures/buttonPress.png')
    assets['man'] = pg.transform.scale(pg.image.load('textures/man.png'), (50, 46))
    assets['manSad'] = pg.transform.scale(pg.image.load('textures/manSad.png'), (128, 128))
    assets['bg'] = pg.image.load('textures/bg.png')
    assets['girl'] = pg.transform.scale(pg.image.load('textures/girl.png'), (54, 46))
    assets['villain'] = pg.transform.scale(pg.image.load('textures/villain.png'), (41, 60))
    assets['bg1'] = pg.transform.scale(pg.image.load('textures/bg1.png'), (644, 400))
    assets['space'] = pg.transform.scale(pg.image.load('textures/space.png'), (400, 100))
    assets['spacePress'] = pg.transform.scale(pg.image.load('textures/spacePress.png'), (400, 100))
    assets['keyboard'] = pg.transform.scale(pg.image.load('textures/keyboard.png'), (295, 100))
    assets['upPress'] = pg.transform.scale(pg.image.load('textures/upPress.png'), (98, 49))
    assets['leftPress'] = pg.transform.scale(pg.image.load('textures/leftPress.png'), (95, 100))
    assets['rightPress'] = pg.transform.scale(pg.image.load('textures/rightPress.png'), (95, 100))
    assets['fire'] = [
        pg.transform.scale(pg.image.load('textures/fire1.png'), (42, 50)),
        pg.transform.scale(pg.image.load('textures/fire2.png'), (45, 50)),
        pg.transform.scale(pg.image.load('textures/fire3.png'), (45, 50)),
    ]
    assets['pipe'] = pg.transform.scale(pg.image.load('textures/pipe.png'), (48, 96))
    # Load fonts
    assets['font_large'] = pg.font.Font('textures/font.ttf', 114)
    assets['font_medium'] = pg.font.Font('textures/font.ttf', 24)
    assets['font_small'] = pg.font.Font('textures/font.ttf', 18)
    # Text Renderings
    assets['play_text'] = assets['font_medium'].render('PLAY!', True, (0, 0, 0))
    assets['controls_text'] = assets['font_medium'].render('CONTROLS', True, (0, 0, 0))
    assets['title_text'] = assets['font_large'].render('BIPPY', True, (236, 180, 28))
    assets['go_text'] = assets['font_large'].render('SAVE FIPPY!', True, (236, 180, 28))
    assets['end_text'] = assets['font_large'].render('GAME OVER', True, (236, 180, 28))
    assets['jump_text'] = assets['font_medium'].render('JUMP - space bar or up arrow', True, (0, 0, 0))
    assets['move_text'] = assets['font_medium'].render('MOVE - left or right arrow', True, (0, 0, 0))
    assets['back_text'] = assets['font_small'].render('BACK', True, (0, 0, 0))
    assets['restart_text'] = assets['font_medium'].render('RESTART', True, (0, 0, 0))
    # Dialogue Texts
    assets['fippy1_text'] = assets['font_medium'].render('Hey Bippy <3', True, (0, 0, 0))
    assets['fippy2_text'] = assets['font_medium'].render('AHHH! HELP!', True, (0, 0, 0))
    assets['bippy1_text'] = assets['font_medium'].render('Hey Fippy <3', True, (0, 0, 0))
    assets['bippy2_text'] = assets['font_medium'].render('FIPPY WATCH OUT!', True, (0, 0, 0))
    assets['bippy3_text'] = assets['font_medium'].render('I\'LL SAVE YOU!', True, (0, 0, 0))
    assets['villain1_text'] = assets['font_medium'].render('I got you now Fippy!', True, (0, 0, 0))
    return assets

# Object Classes
class Obstacle(pg.sprite.Sprite):
    def __init__(self, x, speed, assets):
        super().__init__()
        self.image = random.choice(assets['fire'])
        self.rect = self.image.get_rect(midbottom=(x, 376))
        self.speed = speed
        self.pipe_image = assets['pipe']
    
    def update(self):
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.kill()
    
    def draw(self, surface):
        surface.blit(self.image, self.rect)
        pipe_rect = self.pipe_image.get_rect(midtop=(self.rect.centerx, self.rect.bottom))
        surface.blit(self.pipe_image, pipe_rect)

class Player(pg.sprite.Sprite):
    def __init__(self, x, y, assets):
        super().__init__()
        self.image = assets['man']
        self.rect = self.image.get_rect(topleft=(x, y))
        self.vel_y = 0
        self.is_jumping = False
        self.assets = assets
    
    def update(self, keys_pressed):
        if not self.is_jumping:
            if keys_pressed[pg.K_SPACE] or keys_pressed[pg.K_UP]:
                self.is_jumping = True
                self.vel_y = -12
        if self.is_jumping:
            self.vel_y += 0.5  # Gravity
            self.rect.y += self.vel_y
            if self.rect.bottom >= 376:
                self.rect.bottom = 376
                self.is_jumping = False
                self.vel_y = 0
        if keys_pressed[pg.K_LEFT]:
            self.rect.x -= 5
            if self.rect.left < 0:
                self.rect.left = 0
        if keys_pressed[pg.K_RIGHT]:
            self.rect.x += 5
            if self.rect.right > SCREEN_WIDTH:
                self.rect.right = SCREEN_WIDTH

class Game:
    def __init__(self):
        self.assets = load_assets()
        self.state = TITLE
        self.player = Player(50, 330, self.assets)
        self.obstacles = pg.sprite.Group()
        self.bg_x = 0
        self.bg_speed = 3
        self.score = 0
        self.last_obstacle_time = 0
        self.obstacle_interval = 1500  # milliseconds
        self.start_time = pg.time.get_ticks()
        # Intro scene variables
        self.intro_player_x = -50
        self.intro_player_y = 330
        self.intro_villain_x = 630
        self.intro_girl_x = 400
        self.intro_dialogue_time = pg.time.get_ticks()
        self.intro_stage = 0  # To keep track of dialogue stages

    def reset(self):
        self.player = Player(50, 330, self.assets)
        self.obstacles = pg.sprite.Group()
        self.bg_x = 0
        self.score = 0
        self.start_time = pg.time.get_ticks()
        self.last_obstacle_time = 0
        # Reset intro scene variables
        self.intro_player_x = -50
        self.intro_player_y = 330
        self.intro_villain_x = 630
        self.intro_girl_x = 400
        self.intro_dialogue_time = pg.time.get_ticks()
        self.intro_stage = 0

    def run(self):
        running = True
        while running:
            keys_pressed = pg.key.get_pressed()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
            if self.state == TITLE:
                self.title_screen()
            elif self.state == CONTROLS:
                self.controls_screen()
            elif self.state == INTRO:
                self.intro_screen()
            elif self.state == PLAYING:
                self.playing_screen(keys_pressed)
            elif self.state == GAME_OVER:
                self.game_over_screen()
            pg.display.flip()
            clock.tick(FPS)
        pg.quit()
        sys.exit()

    def title_screen(self):
        screen.blit(self.assets['bg'], (0, 0))
        # Draw Title
        title_text = self.assets['title_text']
        screen.blit(title_text, (SCREEN_WIDTH//2 - title_text.get_width()//2, 80))
        # Draw Buttons
        mouse_x, mouse_y = pg.mouse.get_pos()
        play_button_rect = pg.Rect(210, 245, 180, 44)
        controls_button_rect = pg.Rect(210, 295, 180, 44)
        pg.mouse.set_cursor(pg.SYSTEM_CURSOR_ARROW)
        if play_button_rect.collidepoint(mouse_x, mouse_y):
            pg.mouse.set_cursor(pg.SYSTEM_CURSOR_HAND)
            screen.blit(self.assets['buttonPress'], play_button_rect.topleft)
            if pg.mouse.get_pressed()[0]:
                self.state = INTRO
                self.intro_dialogue_time = pg.time.get_ticks()
        else:
            screen.blit(self.assets['button'], play_button_rect.topleft)
        if controls_button_rect.collidepoint(mouse_x, mouse_y):
            pg.mouse.set_cursor(pg.SYSTEM_CURSOR_HAND)
            screen.blit(self.assets['buttonPress'], controls_button_rect.topleft)
            if pg.mouse.get_pressed()[0]:
                self.state = CONTROLS
        else:
            screen.blit(self.assets['button'], controls_button_rect.topleft)
        # Draw Button Text
        play_text = self.assets['play_text']
        controls_text = self.assets['controls_text']
        screen.blit(play_text, (play_button_rect.centerx - play_text.get_width()//2, play_button_rect.centery - play_text.get_height()//2))
        screen.blit(controls_text, (controls_button_rect.centerx - controls_text.get_width()//2, controls_button_rect.centery - controls_text.get_height()//2))

    def controls_screen(self):
        screen.fill((89, 153, 255))
        # Handle Back Button
        mouse_x, mouse_y = pg.mouse.get_pos()
        back_button_rect = pg.Rect(10, 10, 120, 29)
        pg.mouse.set_cursor(pg.SYSTEM_CURSOR_ARROW)
        if back_button_rect.collidepoint(mouse_x, mouse_y):
            pg.mouse.set_cursor(pg.SYSTEM_CURSOR_HAND)
            screen.blit(pg.transform.scale(self.assets['buttonPress'], (120, 29)), back_button_rect.topleft)
            if pg.mouse.get_pressed()[0]:
                self.state = TITLE
        else:
            screen.blit(pg.transform.scale(self.assets['button'], (120, 29)), back_button_rect.topleft)
        back_text = self.assets['back_text']
        screen.blit(back_text, (back_button_rect.centerx - back_text.get_width()//2, back_button_rect.centery - back_text.get_height()//2))
        # Display Controls
        keys = pg.key.get_pressed()
        screen.blit(self.assets['keyboard'], (153, 170))
        if keys[pg.K_SPACE]:
            screen.blit(self.assets['spacePress'], (100, 50))
        else:
            screen.blit(self.assets['space'], (100, 50))
        if keys[pg.K_UP]:
            screen.blit(self.assets['upPress'], (153 + 99, 170))
        if keys[pg.K_LEFT]:
            screen.blit(self.assets['leftPress'], (153, 170))
        if keys[pg.K_RIGHT]:
            screen.blit(self.assets['rightPress'], (153 + 200, 170))
        # Instructions
        jump_text = self.assets['jump_text']
        move_text = self.assets['move_text']
        screen.blit(jump_text, (160, 300))
        screen.blit(move_text, (173, 350))

    def intro_screen(self):
        # Intro scene logic
        current_time = pg.time.get_ticks()
        elapsed_time = (current_time - self.intro_dialogue_time) / 1000  # Convert to seconds
        screen.blit(self.assets['bg1'], (0, 0))
        pg.mouse.set_cursor(pg.SYSTEM_CURSOR_ARROW)
        keys = pg.key.get_pressed()

        # Draw characters
        screen.blit(self.assets['man'], (self.intro_player_x, self.intro_player_y))
        screen.blit(self.assets['girl'], (self.intro_girl_x, 330))
        screen.blit(self.assets['villain'], (self.intro_villain_x, 316))

        # Bippy moves right
        if self.intro_player_x < 160:
            self.intro_player_x += 4
        else:
            self.intro_player_x = 160

        # Dialogue sequence
        if elapsed_time <= 3:
            # Fippy says "Hey Bippy <3"
            screen.blit(self.assets['fippy1_text'], (360, 300))
        elif elapsed_time <= 5:
            # Bippy says "Hey Fippy <3"
            screen.blit(self.assets['bippy1_text'], (120, 300))
        elif elapsed_time <= 6:
            # Villain moves towards Fippy
            if self.intro_villain_x > 460:
                self.intro_villain_x -= 4
        elif elapsed_time <= 8:
            # Bippy says "FIPPY WATCH OUT!"
            screen.blit(self.assets['bippy2_text'], (120, 300))
            # Villain says "I got you now Fippy!"
            screen.blit(self.assets['villain1_text'], (self.intro_villain_x - 80, 286))
        elif elapsed_time <= 10:
            # Villain takes Fippy away
            self.intro_girl_x = self.intro_villain_x - 54
            self.intro_villain_x += 4
            screen.blit(self.assets['fippy2_text'], (self.intro_girl_x - 40, 300))
        elif elapsed_time <= 12:
            # Bippy says "I'LL SAVE YOU!"
            screen.blit(self.assets['bippy3_text'], (120, 300))
        else:
            # Start the game
            self.state = PLAYING
            self.start_time = pg.time.get_ticks()
            return

        # Allow skipping the intro with UP key
        if keys[pg.K_UP]:
            self.state = PLAYING
            self.start_time = pg.time.get_ticks()
            return

    def playing_screen(self, keys_pressed):
        # Background scrolling
        self.bg_x -= self.bg_speed
        bg_width = self.assets['bg1'].get_width()
        if self.bg_x <= -bg_width:
            self.bg_x = 0
        screen.blit(self.assets['bg1'], (self.bg_x, 0))
        screen.blit(self.assets['bg1'], (self.bg_x + bg_width, 0))
        # Update player
        self.player.update(keys_pressed)
        screen.blit(self.player.image, self.player.rect)
        # Spawn Obstacles
        current_time = pg.time.get_ticks()
        if current_time - self.last_obstacle_time > self.obstacle_interval:
            obstacle_x = SCREEN_WIDTH + random.randint(0, 100)
            obstacle = Obstacle(obstacle_x, self.bg_speed, self.assets)
            self.obstacles.add(obstacle)
            self.last_obstacle_time = current_time
        # Update Obstacles
        self.obstacles.update()
        for obstacle in self.obstacles:
            obstacle.draw(screen)
        # Collision Detection
        if pg.sprite.spritecollideany(self.player, self.obstacles):
            self.state = GAME_OVER
        # Update Score
        self.score += 1
        score_text = self.assets['font_medium'].render(str(self.score), True, (0, 0, 0))
        screen.blit(score_text, (20, 20))
        # Display "SAVE FIPPY!" for first few seconds
        elapsed_time = (current_time - self.start_time) / 1000
        if elapsed_time <= 3:
            go_text = self.assets['go_text']
            screen.blit(go_text, (SCREEN_WIDTH//2 - go_text.get_width()//2, 50))

    def game_over_screen(self):
        screen.fill((79, 112, 239))
        # Display Game Over Text
        game_over_text = self.assets['end_text']
        screen.blit(game_over_text, (SCREEN_WIDTH//2 - game_over_text.get_width()//2, 50))
        # Display Score
        score_text = self.assets['font_medium'].render(f'Your Score: {self.score}', True, (0, 0, 0))
        screen.blit(score_text, (SCREEN_WIDTH//2 - score_text.get_width()//2, 200))
        # Display Sad Bippy
        screen.blit(self.assets['manSad'], (SCREEN_WIDTH//2 - self.assets['manSad'].get_width()//2, 140))
        # Restart Button
        mouse_x, mouse_y = pg.mouse.get_pos()
        restart_button_rect = pg.Rect(210, 340, 180, 44)
        pg.mouse.set_cursor(pg.SYSTEM_CURSOR_ARROW)
        if restart_button_rect.collidepoint(mouse_x, mouse_y):
            pg.mouse.set_cursor(pg.SYSTEM_CURSOR_HAND)
            screen.blit(self.assets['buttonPress'], restart_button_rect.topleft)
            if pg.mouse.get_pressed()[0]:
                self.reset()
                self.state = TITLE
        else:
            screen.blit(self.assets['button'], restart_button_rect.topleft)
        restart_text = self.assets['restart_text']
        screen.blit(restart_text, (restart_button_rect.centerx - restart_text.get_width()//2, restart_button_rect.centery - restart_text.get_height()//2))

if __name__ == '__main__':
    game = Game()
    game.run()