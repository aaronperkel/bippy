# src/main.py
import pygame as pg
from .settings import SCREEN_WIDTH, SCREEN_HEIGHT, TITLE, FPS
from .assets import AssetManager
from .states.state_machine import StateMachine
from .states.title_state import TitleState

def main():
    pg.init()
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pg.display.set_caption(TITLE)
    clock = pg.time.Clock()
    assets = AssetManager()
    state_machine = StateMachine()
    state_machine.add_state('title', TitleState(state_machine, assets))
    state_machine.change_state('title')
    running = True
    while running:
        dt = clock.tick(FPS) / 1000
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                running = False
        state_machine.update(dt, events)
        state_machine.draw(screen)
        pg.display.flip()
    pg.quit()

if __name__ == '__main__':
    main()