import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
from dotenv import load_dotenv
from otp_generate import generate_otp

load_dotenv()

port = 587
email_server = "smtp.gmail.com"
email_sender = os.getenv("email_id")
email_pass = os.getenv("email_pass")

def send_mail(rec,sub,body):
    try:
        msg = MIMEMultipart()
        msg['From']=email_sender
        msg['To']=rec
        msg['Subject']=sub
        msg.attach(MIMEText(body,'plain'))

        with smtplib.SMTP(email_server,port) as server:
            server.starttls()
            server.login(email_sender,email_pass)
            server.sendmail(email_sender,rec,msg.as_string()) 

        print("Email sent successfully!")

    except Exception as e:
        print(f"Error for email sending: {e}")

if __name__=="__main__":
    rec="dhyan0962@gmail.com"

    otp = generate_otp()
    print("Generated OTP:", otp)

    sub="Your Email Verification OTP"
    body = f"""
Hello,

Your OTP is:

{otp}

Please do not share this OTP with anyone.

Thank you.
"""
    send_mail(rec,sub,body)