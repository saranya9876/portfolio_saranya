from flask import Flask, render_template, request
import smtplib
from email.mime.text import MIMEText


app = Flask(__name__, static_url_path='/static')
@app.route('/')
def index():
    return render_template('index.html')

# This is the route for the contact form
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']

        # Replace these variables with your email credentials and settings
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587
        sender_email = 'saranyasarusiva9999@gmail.com'
        sender_password = 'bpstpkuirlatvydv'
        receiver_email = 'saranya.21iamos124@iadc.ac.in'

        # Create the email message
        msg = MIMEText(message)
        msg['Subject'] = subject
        msg['From'] = sender_email
        msg['To'] = receiver_email

        # Send the email
        try:
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.login(sender_email, sender_password)
                server.send_message(msg)
            return 'success'
        except Exception as e:
            print(f"Error: {e}")
            return 'error'

    return render_template('contact_form.html')  # Replace 'contact_form.html' with your actual HTML file for the contact form


if __name__ == '__main__':
    app.run(debug=True)
