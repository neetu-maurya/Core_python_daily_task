#5. Python program to check the validity of password input by users

import re

# Function to check password validity
def is_valid_password(password):
    # Check length
    if len(password) < 8:
        return "Password must be at least 8 characters long."

    # Check for uppercase letter
    if not any(char.isupper() for char in password):
        return "Password must contain at least one uppercase letter."

    # Check for lowercase letter
    if not any(char.islower() for char in password):
        return "Password must contain at least one lowercase letter."

    # Check for a digit
    if not any(char.isdigit() for char in password):
        return "Password must contain at least one number."

    # Check for special character
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "Password must contain at least one special character."

    # If all conditions are met
    return "Password is valid."

# User input
password = input("Enter your password: ")

# Check validity and display the result
result = is_valid_password(password)
print(result)

