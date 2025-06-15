# Number Guessing Game

# generate a random number between 1 and 100
import random 
number_to_guess = random.randint(1, 100)

# prompt the user to guess the number
guess = None
attempts = 0
print("Welcome to the Number Guessing Game!")

# Loop until the user guesses the number or runs out of attempts
while guess != number_to_guess:
    # Check if the user has reached the maximum number of attempts
    if attempts == 10:
        print("Sorry, you've used all your attempts! The number was " + 
              f"{number_to_guess}. Better luck next time! 🎯")
        break
    
    # Prompt the user for a guess
    guess = int(input("Guess a number between 1 and 100: "))
    
    # Increment the attempt counter
    attempts += 1
    
    # Provide feedback on the guess
    if guess < number_to_guess:
        print("Too low! Try again.")
    elif guess > number_to_guess:
        print("Too high! Try again.")
    else:
        print("Congratulations! You've guessed the number! 🎉" + 
              f"It took you {attempts} attempts to guess the number {number_to_guess}.")