class VacuumCleaner:
    def __init__(self, initial_state):
        self.state = initial_state
        self.position = 'A'

    def clean(self):
        print(f"Initial state: {self.state}, Vacuum at {self.position}")
        steps = 0
        while not self.is_goal_state():
            if self.state[self.position] == 'Dirty':
                self.state[self.position] = 'Clean'
                print(f"Cleaning {self.position}... State: {self.state}")
            elif self.position == 'A':
                self.position = 'B'
                print(f"Moving to {self.position}... State: {self.state}")
            elif self.position == 'B':
                self.position = 'A'
                print(f"Moving to {self.position}... State: {self.state}")
            steps += 1
        print(f"Goal state reached: {self.state} in {steps} steps")

    def is_goal_state(self):
        return self.state['A'] == 'Clean' and self.state['B'] == 'Clean'

# Example usage:
initial_state = {'A': 'Dirty', 'B': 'Dirty'}
vacuum_cleaner = VacuumCleaner(initial_state)
vacuum_cleaner.clean()
