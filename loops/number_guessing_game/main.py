# Number Guessing Game

# generate a random number between 1 and 100
import random 
number_to_guess = random.randint(1, 100)

# prompt the user to guess the number
guess = None
attempts = 0
print("Welcome to the Number Guessing Game!")

while guess != number_to_guess:
    guess = int(input("Guess a number between 1 and 100: "))
    attempts += 1
    if guess < number_to_guess:
        print("Too low! Try again.")
    elif guess > number_to_guess:
        print("Too high! Try again.")
    else:
        print("Congratulations! You've guessed the number! 🎉" + 
              f"It took you {attempts} attempts to guess the number {number_to_guess}.")