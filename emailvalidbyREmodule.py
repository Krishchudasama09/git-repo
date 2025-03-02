import re

class EmailValidator:
    # Ensures a valid domain and a proper extension (like .com, .in, .org)
    pattern = r"^[a-zA-Z0-9._]+@[a-zA-Z0-9-]+\.(com|in|org|net|edu|gov)$"

    @staticmethod
    def validate(email):
        if re.match(EmailValidator.pattern, email):
            print("Valid email")
        else:
            print("Invalid email")

# Example usage
user_email = input("Enter your email: ")
EmailValidator.validate(user_email)