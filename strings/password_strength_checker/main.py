# Password Strength Checker

# input password
password = input("Enter a password to check its strength: ")

# evaluate password strength
special_characters = "!@#$%^&*()-_=+[]{}|;:',.<>?/"
# check for password length
if len(password) < 8:
    print("Weak password: Password must be at least 8 characters long.")

# check for uppercase, lowercase, digits, and special characters
elif (not any(c.isupper() for c in password) or
      not any(c.islower() for c in password) or
      not any(c.isdigit() for c in password) or
      not any(c in special_characters for c in password)):
    missing_requirements = []

    if not any(c.isupper() for c in password):
        missing_requirements.append("an uppercase letter")
    if not any(c.islower() for c in password):
        missing_requirements.append("a lowercase letter")
    if not any(c.isdigit() for c in password):
        missing_requirements.append("a digit")
    if not any(c in special_characters for c in password):
        missing_requirements.append("a special character")

    if missing_requirements:
        print(f"Weak password: Missing {', '.join(missing_requirements)}.")

# if all conditions are met, the password is strong
else:
    print("Strong password: Your password meets all the strength requirements! 🎉")