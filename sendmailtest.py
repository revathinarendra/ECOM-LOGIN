import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_verification_email(
    smtp_server, smtp_port, smtp_username, smtp_password, recipient_email
):
    try:
        # Create a MIMEText object to represent the email content
        message = MIMEMultipart()
        message["From"] = smtp_username
        message["To"] = recipient_email
        message["Subject"] = "Test Verification Email"

        body = "This is a test verification email. Your account has been successfully verified."
        message.attach(MIMEText(body, "plain"))

        # Establish connection to SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Use TLS
        # Login to the SMTP server
        server.login(smtp_username, smtp_password)
        # Send the email
        server.sendmail(smtp_username, recipient_email, message.as_string())
        print("Verification email sent successfully!")
        server.quit()  # Quit the server
        return True
    except Exception as e:
        print(f"Failed to send verification email: {e}")
        return False


# Replace these variables with your SMTP server details and recipient email address
smtp_server = "smtp.gmail.com"
smtp_port = 587  # For Gmail
smtp_username = "katari.revathi@gmail.com"
smtp_password = "hoqsmuttcrjggflk"
recipient_email = "deepaksaivenkat1111@gmail.com"

# Send verification email
send_verification_email(
    smtp_server, smtp_port, smtp_username, smtp_password, recipient_email
)
