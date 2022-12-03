# Rock Paper Scissors Game in python made by Nuno Mendonça

# imports

import random

# start function to start the game
def play():
    # user input for him to choose is weapon
    user = str(input("Choose your weapon: 'r' for rock, 'p' for paper, 's' for scissors: ")).lower()

    # random choice returns a random choice from a sequence    
    computer = random.choice(["r", "p", "s"])



