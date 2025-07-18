import imaplib
import email
from email.message import EmailMessage
import smtplib
from config import EMAIL_ADDRESS, EMAIL_APP_PASS
from datetime import datetime
from pprint import pprint as pp

class EmailClient:
    def __init__(self):
        self.imap = imaplib.IMAP4_SSL("imap.gmail.com")
        self.imap.login(EMAIL_ADDRESS, EMAIL_APP_PASS)

    def fetch_unread_messages(self):
        today_str = datetime.now().strftime("%d-%b-%Y")
        self.imap.select("inbox")
        # _, message_nums = self.imap.search(None, f'(UNSEEN ON {today_str})')
        _, message_nums = self.imap.search(None, "ALL")
        messages = []
        for num in reversed(message_nums[0].split()): # TODO: REMOVE REVERSE
            _, data = self.imap.fetch(num, "(RFC822)")
            raw_email = data[0][1]
            msg = email.message_from_bytes(raw_email)
            messages.append(msg)
            break # TODO: REMOVE!!! TESTING ONLY <------------------------
        return messages

    def send_reply(self, original_msg, body):
        reply = EmailMessage()
        reply["Subject"] = "Re: " + original_msg["subject"]
        reply["From"] = EMAIL_ADDRESS
        reply["To"] = original_msg["sender"]
        reply.set_content(body)

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_APP_PASS)
            smtp.send_message(reply)
