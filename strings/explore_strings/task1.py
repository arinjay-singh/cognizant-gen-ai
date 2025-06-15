# string slicing and indexing

message = "Python is amazing!"

# extract the word "Python" from the message as the first 6 characters
python_word = message[0:6]

# extract the word "amazing" from the message using negative indexing
amazing_word = message[-8:-1]

# reverse the message using slicing
reversed_message = message[::-1]

# print the extracted words and the reversed message
print(f"First word: {python_word}")
print(f"Amazing part: {amazing_word}")
print(f"Reversed string: {reversed_message}")


