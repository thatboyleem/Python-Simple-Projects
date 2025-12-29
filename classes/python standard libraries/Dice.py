import random

class Die:
    """A class representing a single die."""

    def __init__(self, sides=6):
        """Initialize the die with a default number of sides."""
        self.sides = sides

    def roll(self):
        """Simulate rolling the die and return a random value between 1 and the number of sides."""
        return random.randint(1, self.sides)
die = Die()
for i in range(10):
    print(f"Roll {i+1}: {die.roll()}")