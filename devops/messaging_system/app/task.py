from app.celery_worker import celery_app
import time
import smtplib
import os
from email.message import EmailMessage
from dotenv import load_dotenv
load_dotenv()


SMTP_HOST = os.getenv("SMTP_HOST", "smtp.gmail.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))
SMTP_USER = os.getenv("SMTP_USER")           # e.g. okekolawoles36@gmail.com
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")   # 16-char Google App Password


@celery_app.task
def send_email(recipient):

    print(f"Sending email to {recipient}")

    # remove "mailto:" prefix if present
    if recipient.startswith("mailto:"):
        recipient = recipient.replace("mailto:", "")

    time.sleep(5)

    message = EmailMessage()
    message["From"] = SMTP_USER
    message["To"] = recipient
    message["Subject"] = "Test Email"
    message.set_content("This is a test email from the messaging system.")

    try:
        with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as mail_server:
            mail_server.starttls()
            mail_server.login(SMTP_USER, SMTP_PASSWORD)
            mail_server.send_message(message)

        print(f"Email sent to {recipient}")

        return f"Email sent to {recipient}"

    except Exception as e:
        print(f"Email sending failed: {e}")
        return str(e)