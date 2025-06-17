# using try, except, else and finally

# try block to attempt to divide two numbers
try:
    print("Try Block:")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 / num2
    print()
# except block to catch error if it occurs
except Exception as e:
    print()
    print("Except Block:")
    print(f"An error occurred: {e}")
    print()
# else block to execute if no error occurs
else:
    print("Else Block:")
    print(f"The result is: {result}")
    print()
# finally block to execute regardless of whether an error occurred
finally:
    print("Finally Block:")
    print("This block always executes")