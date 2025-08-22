import re

def password_complexity_checker(password):
    # Check the length of the password
    if len(password) < 8:
        return "Password must be at least 8 characters long."

    # Check for the presence of uppercase letters
    if not re.search(r'[A-Z]', password):
        return "Password must contain at least one uppercase letter."

    # Check for the presence of lowercase letters
    if not re.search(r'[a-z]', password):
        return "Password must contain at least one lowercase letter."

    # Check for the presence of digits
    if not re.search(r'[0-9]', password):
        return "Password must contain at least one digit."

    # Check for the presence of special characters
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return "Password must contain at least one special character."

    return "Password is strong!"

# Example usage
password = input("Enter a password to check: ")
result = password_complexity_checker(password)
print(result)
