import smtplib

# Your SMTP server and port
smtp_server = 'smtp.gmail.com'
smtp_port = 587

# Your email credentials
sender_email = 'saranyasarusiva9999@gmail.com'
sender_password = 'dqoxezokbqcundlt'

# Create an SMTP connection
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()  # Enable TLS encryption

try:
    # Log in to your account
    server.login(sender_email, sender_password)

    # Send a test email
    recipient_email = 'saranya.21iamos124@iadc.ac.in'
    subject = 'Test Email'
    body = 'This is a test email sent from Python.'
    message = f'Subject: {subject}\n\n{body}'
    server.sendmail(sender_email, recipient_email, message)

    print('Test email sent successfully!')
except Exception as e:
    print('Error sending test email:', e)
finally:
    # Close the connection
    server.quit()
