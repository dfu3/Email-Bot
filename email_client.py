import imaplib
import email
from email.message import EmailMessage
import smtplib
from config import EMAIL_ADDRESS, EMAIL_APP_PASS, EMAIL_FILTER
from datetime import datetime

class EmailClient:
    def __init__(self):
        self.imap = imaplib.IMAP4_SSL("imap.gmail.com")
        try:
            self.imap.login(EMAIL_ADDRESS, EMAIL_APP_PASS)
        except smtplib.SMTPAuthenticationError:
            print("❌ Failed to log in to SMTP server. Check your email or app password.")


    def fetch_unread_messages(self):
        today_str = datetime.now().strftime("%d-%b-%Y")
        self.imap.select("inbox")
        _, message_nums = self.imap.search(None, f'({EMAIL_FILTER} ON {today_str})')
        messages = []
        for num in message_nums[0].split():
            _, data = self.imap.fetch(num, "(RFC822)")
            raw_email = data[0][1]
            msg = email.message_from_bytes(raw_email)
            messages.append(msg)
        return messages

    def send_reply(self, original_msg, body):
        try:
            reply = EmailMessage()
            reply["Subject"] = "Re: " + original_msg["subject"]
            reply["From"] = EMAIL_ADDRESS
            reply["To"] = original_msg["sender"]
            reply.set_content(body)

            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
                smtp.login(EMAIL_ADDRESS, EMAIL_APP_PASS)
                smtp.send_message(reply)
        
        except smtplib.SMTPAuthenticationError:
            print("❌ Failed to log in to SMTP server. Check your email or app password.")

        except smtplib.SMTPRecipientsRefused:
            print(f"❌ Recipient address was rejected: {original_msg['sender']}")

        except smtplib.SMTPException as e:
            print(f"❌ SMTP error occurred while sending reply: {e}")

        except Exception as e:
            print(f"❌ Unexpected error during email send: {e}")
