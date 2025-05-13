# Assignent: Exploring Python Concepts
# Task 3 - Conditional Statements: The Number Checker

# get input from the user and cast it to a float
number = float(input("Enter a number: "))

# check if the number is positive, negative, or zero
# print response accordingly
if number > 0:
    print(f"The number {number} is positive.")
elif number < 0:
    print(f"The number {number} is negative.")
else:
    print("The number is zero.")

