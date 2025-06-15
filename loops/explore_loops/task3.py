# Find the factorial

num = int(input("Enter a number to find its factorial: "))

# Initialize the factorial variable
factorial = 1

# Loop to calculate the factorial
for i in range(2, num + 1):
    factorial *= i
    
# Print the result
print(f"The factorial of {num} is {factorial}.")
print("This was calculated by multiplying all integers from 1 to", num, "together! 🎉")