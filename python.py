import re

def check_password_strength(password):
    """
    Function to evaluate the strength of a password based on cybersecurity metrics.
    Developed as part of Decode Labs Cyber Security Project 1.
    """
    score = 0
    feedback = []

    # 1. Length Check
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("- Password is too short (Minimum recommended length is 8 characters).")

    # 2. Uppercase Check
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("- Add at least one uppercase letter (A-Z).")

    # 3. Lowercase Check
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("- Add at least one lowercase letter (a-z).")

    # 4. Digits Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("- Add at least one number (0-9).")

    # 5. Special Characters Check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>_]", password):
        score += 1
    else:
        feedback.append("- Add at least one special character (e.g., @, #, $, %).")

    # Determine Strength Level based on score
    if score >= 5:
        strength = "🟢 Very Strong"
    elif score == 4:
        strength = "🟡 Strong"
    elif score == 3:
        strength = "🟠 Medium"
    else:
        strength = "🔴 Weak"

    return strength, feedback

def main():
    print("=" * 45)
    print("   DECODE LABS - PASSWORD STRENGTH CHECKER   ")
    print("=" * 45)
    
    user_password = input("Enter a password to test: ").strip()
    
    if not user_password:
        print("\n❌ Error: Password cannot be empty!")
        return

    strength, feedback = check_password_strength(user_password)
    
    print("\n" + "-" * 30)
    print(f"Password Strength: {strength}")
    print("-" * 30)
    
    if feedback:
        print("\nSuggestions to improve your password:")
        for tip in feedback:
            print(tip)
    else:
        print("\n✨ Excellent choice! Your password meets all security guidelines.")
    print("=" * 45)

if __name__ == "__main__":
    main()