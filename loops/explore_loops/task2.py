# Multiplication table with for loops

num = int(input("Enter a number to generate its multiplication table: "))

# Loop to generate the multiplication table from 1 to 10
for i in range(1, 11):
    result = num * i
    print(f"{num} x {i} = {result}")
    
# Print a message indicating the end of the multiplication table
print("Multiplication table completed! 🎉")