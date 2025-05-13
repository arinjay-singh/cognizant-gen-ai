# Project: Eligible Elector
# Determine if a person is eligible to vote in the US

# ask user for their age
try:
    age = int(input("Enter your age: "))
except ValueError:
    print("Invalid input. Please enter a valid integer for your age.")
    exit()

# check if the user is eligible to vote
if age >= 18:
    print("Congratulations! You are eligible to vote.")
else:
    print(f"Sorry, you are not eligible to vote yet. Just {18 - age} more years to go!")