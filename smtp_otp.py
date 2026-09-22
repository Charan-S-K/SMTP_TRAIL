import os
import secrets
import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from dotenv import load_dotenv


load_dotenv()


# ============================================================
# SMTP CONFIGURATION
# ============================================================

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

EMAIL_SENDER = os.getenv("email_id")
EMAIL_PASSWORD = os.getenv("email_pass")


# ============================================================
# OTP GENERATION
# ============================================================

def generate_otp():
    return str(secrets.randbelow(900000) + 100000)


# ============================================================
# SEND OTP EMAIL
# ============================================================

def send_otp_email(receiver, otp):

    subject = "Your Email Verification OTP"

    body = f"""
Hello,

Your OTP for email verification is:

{otp}

Please do not share this OTP with anyone.

Thank you.
"""

    try:

        msg = MIMEMultipart()

        msg["From"] = EMAIL_SENDER
        msg["To"] = receiver
        msg["Subject"] = subject

        msg.attach(
            MIMEText(body, "plain")
        )

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:

            server.starttls()

            server.login(
                EMAIL_SENDER,
                EMAIL_PASSWORD
            )

            server.sendmail(
                EMAIL_SENDER,
                receiver,
                msg.as_string()
            )

        return True

    except Exception as e:

        print("Error while sending email:", e)

        return False


# ============================================================
# MAIN PROGRAM
# ============================================================

if __name__ == "__main__":

    receiver = input("Enter your email address: ")

    # Generate OTP
    generated_otp = generate_otp()

    print("\nOTP generated.")

    # Send OTP
    email_sent = send_otp_email(
        receiver,
        generated_otp
    )

    if email_sent:

        print("OTP sent successfully!")
        print("Check your email.")

        # Ask user to enter OTP
        user_otp = input("\nEnter the OTP you received: ")

        # Verify OTP
        if user_otp == generated_otp:

            print("\n✅ OTP verified successfully!")

        else:

            print("\n❌ Invalid OTP!")

    else:

        print("\n❌ OTP could not be sent.")