import re

def password_strength(password):
    score = 0
    remarks = []

    # Length
    if len(password) >= 8:
        score += 1
    else:
        remarks.append("Make the password at least 8 characters long.")

    # Uppercase and Lowercase
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        remarks.append("Use both uppercase and lowercase letters.")

    # Numbers
    if re.search(r'[0-9]', password):
        score += 1
    else:
        remarks.append("Include at least one number.")

    # Special Characters
    if re.search(r'[^A-Za-z0-9]', password):
        score += 1
    else:
        remarks.append("Add special characters like @, #, $, etc.")

    # Common patterns
    common_patterns = ["123", "password", "qwerty", "abc", "111", "000"]
    if any(pattern in password.lower() for pattern in common_patterns):
        remarks.append("Avoid common words or patterns like '123', 'password'.")

    # Score interpretation
    if score <= 2:
        strength = "Weak"
    elif score == 3:
        strength = "Medium"
    else:
        strength = "Strong"

    return strength, remarks

# Test
pwd = input("Enter your password: ")
strength, suggestions = password_strength(pwd)
print(f"\nPassword Strength: {strength}")
if suggestions:
    print("Suggestions:")
    for suggestion in suggestions:
        print("-", suggestion)
