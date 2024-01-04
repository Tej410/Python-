import random

class Dice:
    def roll(self):
        return(f"({random.randint(1,6)},{random.randint(1,6)})")

print(Dice().roll())