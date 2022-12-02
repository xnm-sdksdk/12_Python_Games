# Guess Number Game in python made by Nuno Mendonça


# imports

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
            print(f"You got it! The number was {random_number}")
        
guess(10)
    #
    #