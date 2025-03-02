import re


email_pattern = r"[a-zA-Z0-9.*%±]+@[a-zA-Z0-9.-]+.[a-zA-Z]{2,}"
while True:  
    email = input("Enter your email address: ").strip()  

    if re.match(email_pattern, email):
        print("Valid email.")
        
    else:
        print("Wrong email Please try again.")
