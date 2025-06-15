# Counting Down with Loops

starting_num = int(input("Enter a starting number: "))

# Loop to count down from the starting number to 0
for i in range(starting_num, 0, -1):
    print(i, end=' ')
    
# Print "Blast off!" after the countdown
print("Blast off! 🚀")