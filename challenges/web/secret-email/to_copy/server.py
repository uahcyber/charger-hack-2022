from flask import Flask, render_template, request
import os
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

FLAG = ""
allowedDomain = "c00lblu3h4x0r.gov"

def send_email(email):
    sender_email = os.getenv("CTF_EMAIL")
    sender_password = os.getenv("CTF_EMAIL_PASSWORD")
    receiver_email = email.strip()
    message = MIMEMultipart("alternative")
    message["Subject"] = f"Secret Email Challenge (Charger Hack 2022)"
    message["From"] = sender_email
    message["To"] = receiver_email
    text = f"Here is your flag: {FLAG}"
    part1 = MIMEText(text, "plain")
    message.attach(part1)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, message.as_string())

@app.before_first_request
def read_flag():
    global FLAG
    with open('flag.txt','r') as fp:
        FLAG = fp.readline().strip()

@app.route('/email',methods=["POST"])
def email():
    email = request.json['data']
    if email[-len(allowedDomain):] == allowedDomain and " " not in email:
        send_email(email)
        return "Check your (super cool) email for the flag! Check your spam folder."
    return "Your email is <b>NOT</b> cool enough!"

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)