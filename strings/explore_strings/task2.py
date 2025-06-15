# string methods

message = " hello, python world! "
print(f"Original message: '{message}'")

# strip whitespace from the beginning and end of the message
stripped_message = message.strip()
# print the stripped message
print(f"Stripped message: '{stripped_message}'")

# capitalize the first letter of the message
capitalized_message = stripped_message.capitalize()
# print the capitalized message
print(f"Capitalized message: '{capitalized_message}'")

# replace "world" with "universe"
replaced_message = capitalized_message.replace("world", "universe")
# print the replaced message
print(f"Replaced message: '{replaced_message}'")

# convert string to uppercase
uppercase_message = replaced_message.upper()
# print final message
print(f"Uppercase message: '{uppercase_message}'")