# Rock Paper Scissors Game in python made by Nuno Mendonça

# imports

import random


# Code Logic: r > s, s > p, p > r

# start function to start the game
def play():
    # user input for him to choose is weapon
    user = str(input("Choose your weapon: 'r' for rock, 'p' for paper, 's' for scissors: ")).lower()

    # random choice returns a random choice from a sequence    
    computer = random.choice(["r", "p", "s"])
    
    # if you pass this first if statement, it means that the result is a win or a loss    
    if user == computer:
        return "I can't believe it! It's a tie!"

    # if you get to this conditional then the result is a win or a loss
    if win(user, computer):
        return "You won! Congratulations!"
    
    # if you get to this conditional then the result is a loss
    return "Good try, but you lost!"


def win(user, computer):
    # this function is going to return true if the user wins
    if (user == "r" and computer == "s") or (user == "s" and computer == "p") or (user == "p" and computer == "r"):
        return True
    
# we make this print to show the result of the game and the questions to the user
print(play())