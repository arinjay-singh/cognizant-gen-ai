# check for palindromes in a string

word = input("Enter a word to check if it's a palindrome: ")

# Convert the word to lowercase for case-insensitive comparison
word = word.lower()

# Check if the word is the same forwards and backwards
if word == word[::-1]:
    print(f"{word} is a palindrome!")
else:
    print(f"{word} is not a palindrome.")