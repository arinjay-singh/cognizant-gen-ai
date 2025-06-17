# understanding exceptions in Python

# get user input and handle potential exceptions
while True:
    try:
        num = int(input("Enter a number to divide 100 by: "))
        break
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

# try to perform division and handle division by zero
try:
    result = 100 / num
    print(f"100 divided by {num} is: {result}")
except ZeroDivisionError as e:
    print("Error: Division by zero is not allowed. Please enter a non-zero number.")