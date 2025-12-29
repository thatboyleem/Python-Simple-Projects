import random
from random import choices

class Lottery:
    """A class representing a simple lottery system."""

    def __init__(self, Lottery_list):
        """Initialize the lottery with a range of numbers and letters."""
        if Lottery_list is None:
            Lottery_list = []
        self.Lottery_list = Lottery_list

    def draw_ticket(self, k=4):
        """Draw k random items from the lottery list."""
        return choices(self.Lottery_list, k=k)


# Define the lottery pool
picks = Lottery([1,2,3,4,5,6,7,8,9,10,
                 "A","B","C","D","E","F","G","H","I","J"])

# Your chosen ticket
my_ticket = [7, "A", 3, "C"]

attempts = 0
won = False

while not won:
    attempts += 1
    result = picks.draw_ticket(k=4)
    if result == my_ticket:
        won = True
        print("The winning ticket numbers/letters are:", result)
        print("Any ticket that matches these 4 wins")
        print(f"It took {attempts} attempts to win!")
