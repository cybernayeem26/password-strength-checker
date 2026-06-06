import re

password = input("Enter your password: ")

score = 0
recommendations = []


if len(password) >= 8:
    print("Password length is valid")
    score += 1
else:
    print("Password must be at least 8 characters long")
    recommendations.append("Use at least 8 characters")

if re.search(r"[A-Z]", password):
    print("Contains uppercase letter")
    score += 1
else:
    print("Missing uppercase letter")
    recommendations.append("Add at least one uppercase letter")

if re.search(r"[a-z]", password):
    print("Contains lowercase letter")
    score += 1
else:
    print("Missing lowercase letter") 
    recommendations.append("Add at least one lowercase letter")

if re.search(r"\d", password):
    print("Contains number")
    score += 1
else:
    print("Missing number")
    recommendations.append("Add at least one number")

if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
    print("Contains special character")
    score += 1
else:
    print("Missing special character")
    recommendations.append("Add at least one special character")

common_passwords = [
    "password",
    "123456",
    "admin",
    "qwerty",
    "welcome",
    "letmein"
]

if password.lower() in common_passwords:
    print("\nWARNING: Common password detected!")
    recommendations.append("Avoid commonly used passwords")

if re.search(r"(.)\1{2,}", password):
    print("Warning: Repeated characters detected")
    recommendations.append("Avoid repeated characters")

if score <= 2:
    strength = "Weak"
elif score == 3:
    strength = "Medium"
elif score == 4:
    strength = "Strong"
else:
    strength = "Very Strong"

print("\n" + "=" * 40)
print("PASSWORD STRENGTH REPORT")
print("=" * 40)

print(f"Final Score: {score}/5")
print("Password Strength:", strength)

if recommendations:
    print("\nRecommendations:")
    for item in recommendations:
        print("-", item)
else:
    print("\nExcellent! Your password follows strong security practices.")

