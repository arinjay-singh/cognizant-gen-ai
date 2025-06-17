# calculator 

# import logging txt file to track errors
import logging

# set up logging to capture errors
logging.basicConfig(filename='error_log.txt', level=logging.ERROR)

# function to get a number from the user with error handling
def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError as e:
            print("Invalid input! Please enter a valid number.")
            logging.error(f"ValueError occurred: {e}")

# function to perform the calculator operations
def calculator():
    # welcome message
    print("Welcome to the Error-Free Calculator!")
    
    # main loop for calculator operations
    while True:
        print("\nChoose an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")
        choice = input("> ")

        # handle exit option
        if choice == '5':
            print("Goodbye!")
            break

        # validate choice
        if choice not in {'1', '2', '3', '4'}:
            print("Invalid choice! Please select a valid option.")
            continue

        # get numbers from user
        num1 = get_number("Enter the first number: ")
        num2 = get_number("Enter the second number: ")

        # perform the chosen operation
        try:
            if choice == '1':
                result = num1 + num2
                print(f"Result: {result}")
            elif choice == '2':
                result = num1 - num2
                print(f"Result: {result}")
            elif choice == '3':
                result = num1 * num2
                print(f"Result: {result}")
            elif choice == '4':
                # handle division with error handling
                try:
                    result = num1 / num2
                except ZeroDivisionError as e:
                    print("Oops! Division by zero is not allowed.")
                    logging.error(f"ZeroDivisionError occurred: {e}")
                else:
                    print(f"Result: {result}")
        # handle unexpected errors
        except Exception as e:
            print("An unexpected error occurred.")
            logging.error(f"Unexpected error: {e}")
        # else block to execute if no error occurs
        finally:
            print("Operation completed. You can choose another operation or exit.")

# run the calculator function
calculator()