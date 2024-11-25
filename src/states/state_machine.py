# src/states/state_machine.py
class StateMachine:
    def __init__(self):
        self.states = {}
        self.current_state = None

    def add_state(self, name, state):
        self.states[name] = state

    def change_state(self, name):
        self.current_state = self.states[name]

    def update(self, dt, events):
        if self.current_state:
            self.current_state.update(dt, events)

    def draw(self, surface):
        if self.current_state:
            self.current_state.draw(surface)