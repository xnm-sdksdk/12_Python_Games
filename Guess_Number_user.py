# Guess NUmber Game by Nuno Mendonça


# import random - to generate random numbers
import random

# guess function
def guess(n):
    # generates a random number between 1 and n which is the generated number
    random_number = random.randint(1, n)
    
    
    # we want to run the while loop, while the guess is not correct
    tries = 0
    while tries != random_number:
        # user input to guess the number
        answer = int(input(f"Guess a number between 1 and {n}: "))
        
        # conditional structure to check if the guess is lower then the answer
        if answer < random_number:
            print("Too low, try again!")
        # conditional structure to check if the guess is higher then the answer
        elif answer > random_number:
            print("Too high, try again!")
        # conditional structure to check if the guess is equal to the answer
        else:    
            print(f'You got it! The number was {random_number} correct!')
            print("Until next time!")
            break
        
# function to let computer guess a number that your think
def computer_guess(y):
    # between 1
    low = 1
    # and y
    high = y
    
    feedback = ""
    while feedback != "c" and low != high:
        guess = random.randint(low, high)
        feedback = str(input(f"Is {guess} to high (h) ? Too low (l) ? or correct (c) ? ")).lower()
        
        # conditional structure to check if the feedback is too low
        if feedback == "h":
            # guess minus 1 because the guess is too high and we want to guess lower
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    
    # if the computer guesses right
    print("Yay! The computer guessed your number, {0}, correctly!" .format(guess))
        
computer_guess(10)