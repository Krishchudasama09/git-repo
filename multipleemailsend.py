import smtplib

# Email details
sender_email = 'iamkrish1640@gmail.com'
receiver_email = 'krishchudasma07@gmail.com'
password = 'krish@1640'  # Use an App Password if 2FA is enabled
subject = "Test Python"
body = "I love Python"
message = f"Subject: {subject}\n\n{body}"

try:
    # Establish a connection to the SMTP server
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.ehlo()  # Identify yourself to the server
        server.starttls()  # Upgrade the connection to secure
        server.ehlo()  # Re-identify yourself after encryption
        server.login(sender_email, password)  # Log in to the server
        server.sendmail(sender_email, receiver_email, message)  # Send the email
        print("Email sent successfully!")
except Exception as e:
    print(f"Error: {e}")