
class MessageProcessor:
    def parse_email(self, email_msg):
        subject = email_msg["Subject"]
        sender = email_msg["From"]
        payload = email_msg.get_payload(decode=True)
        body = payload.decode(errors="ignore") if payload else ""
        return {
            "subject": subject,
            "sender": sender,
            "body": body.strip()
        }
