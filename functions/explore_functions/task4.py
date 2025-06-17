# Understanding recursion

def factorial(n):
    """Calculate the factorial of a number using recursion."""
    # base case: if n is 0 or 1, return 1
    if n == 0 or n == 1:
        return 1
    # recursive case: n * factorial of (n-1)
    else:
        return n * factorial(n - 1)
    
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
    
# test the functions
print("Factorial of 5 is:", factorial(5))  # Output: 120
print("The 6th Fibonacci number is", fibonacci(6))  # Output: 8