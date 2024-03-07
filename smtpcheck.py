import smtplib


def test_smtp_connection(smtp_server, smtp_port, smtp_username, smtp_password):
    try:
        # Establish connection to SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Use TLS
        # Login to the SMTP server
        server.login(smtp_username, smtp_password)
        print("SMTP connection successful!")
        server.quit()  # Quit the server
        return True
    except Exception as e:
        print(f"SMTP connection failed: {e}")
        return False


# Replace these variables with your SMTP server details
smtp_server = "smtp.gmail.com"
smtp_port = 587  # For Gmail
smtp_username = "katari.revathi@gmail.com"
smtp_password = "hoqsmuttcrjggflk"

# Test SMTP connection
test_smtp_connection(smtp_server, smtp_port, smtp_username, smtp_password)
