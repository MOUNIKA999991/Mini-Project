import re
def password_strength(password, personal_info):
    length_weight = 1
    uppercase_weight = 2
    lowercase_weight = 2
    digit_weight = 2
    special_char_weight = 2
    score = 0
    feedback = []
    matched_info = {}
    if len(password) >= 12:
        score += length_weight * len(password)
    else:
        feedback.append("Password length is too short.")
    if re.search(r'[A-Z]', password):
        score += uppercase_weight
    else:
        feedback.append("Include at least one uppercase letter.")
    if re.search(r'[a-z]', password):
        score += lowercase_weight
    else:
        feedback.append("Include at least one lowercase letter.")
    if re.search(r'[0-9]', password):
        score += digit_weight
    else:
        feedback.append("Include at least one digit.")

    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += special_char_weight
    else:
        feedback.append("Include at least one special character.")
    personal_info_categories = {
        "name": "full name",
        "date of birth": "date of birth",
        "identity number": "identity number",
        "email address": "email",
        "phone number": "phone number"
    }
    for info_category, info_value in personal_info.items():
        if info_value.lower() in password.lower():
            matched_info[info_category] = info_value
            feedback.append(f"Use personal info in your password in a secure way!")
    return score, feedback, matched_info
def get_strength_category(score):
    if score < 5:
        return "Very Weak"
    elif score < 15:
        return "Weak"
    elif score < 20:
        return "Moderate"
    elif score < 25:
        return "Strong"
    else:
        return "Very Strong"
def evaluate_password(password, personal_info):
    score, feedback, matched_info = password_strength(password, personal_info)
    strength_category = get_strength_category(score)
    return score, strength_category, feedback, matched_info
def main():
    personal_info = {
        "name": input("Enter your full name: "),
        "date of birth": input("Enter your date of birth (YYYYMMDD): "),
        "identity number": input("Enter your identity number: "),
        "email address": input("Enter your email address: "),
        "phone number": input("Enter your phone number: "),
    }
    password = input("Enter your password: ")
    score, strength, feedback, matched_info = evaluate_password(password, personal_info)
    print(f"Password strength: {strength}")
    print(f"Password score: {score}")
    if strength in ["Strong", "Very Strong"]:
        print("Congratulations! Your password is strong and secure.")
    elif strength == "Moderate":
        print("Your password is moderately strong.")
    elif strength == "Weak":
        print("Your password is weak. Please consider making it stronger.")
    elif strength == "Very Weak":
        print("Your password is very weak. Please choose a stronger one.")
    if matched_info:
        print("Personal information found in the password:")
        for info_category, info_value in matched_info.items():
            print(f"- {info_category.capitalize()}: {info_value}")
    if not matched_info:
        print("Personal information not found in the password.")
    if feedback:
        print("Suggestions to improve your password:")
        for suggestion in feedback:
            print(f"- {suggestion}")
if __name__ == "__main__":
    main()

