# Menu of Recursive Functions

# compute factorial using recursion
def factorial(n):
    """Calculate the factorial of a number using recursion."""
    # base case: if n is 0 or 1, return 1
    if n == 0 or n == 1:
        return 1
    # recursive case: n * factorial of (n-1)
    else:
        return n * factorial(n - 1)

# compute nth Fibonacci number using recursion
def fibonacci(n):
    """Calculate the nth Fibonacci number using recursion."""
    # base case: if n is 0, return 0; if n is 1, return 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # recursive case: sum of the two preceding numbers
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
# print welcome message
print("Welcome to the Recursive Functions Program\n")
  
# while loop to display menu and handle user input  
while True:
    # Display the menu options
    print("\nMenu of Recursive Functions:")
    print("1. Calculate Factorial")
    print("2. Calculate Fibonacci Number")
    print("3. Exit")
    
    # Get user input for menu choice
    choice = input("Enter your choice (1-3): ")
    
    # if choice is 1, calculate factorial
    if choice == '1':
        # try-except block to handle invalid input
        try:
            num = int(input("Enter a number to calculate its factorial: "))
            if num < 0:
                raise ValueError("Factorial is not defined for negative numbers. Please try again.")
            print(f"Factorial of {num} is: {factorial(num)}")
        except ValueError as e:
            print("This function only accepts non-negative integers. Please try again.")
    # if choice is 2, calculate Fibonacci number
    elif choice == '2':
        # try-except block to handle invalid input
        try:
            num = int(input("Enter a number to calculate its Fibonacci number: "))
            if num < 0:
                raise ValueError("Fibonacci is not defined for negative numbers. Please try again.")
            print(f"The {num}th Fibonacci number is: {fibonacci(num)}")
        except ValueError as e:
            print("This function only accepts non-negative integers. Please try again.")
    # if choice is 3, exit the program   
    elif choice == '3':
        print("Exiting the program.")
        break
    # if choice is invalid, prompt user to try again   
    else:
        print("Invalid choice, please try again.")
        
