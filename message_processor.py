
class MessageProcessor:
    def parse_email(self, email_msg):
        subject = email_msg["Subject"]
        sender = email_msg["From"]

        body = ""

        if email_msg.is_multipart():
            for part in email_msg.walk():
                content_type = part.get_content_type()
                content_disposition = str(part.get("Content-Disposition"))

                if content_type == "text/plain" and "attachment" not in content_disposition:
                    payload = part.get_payload(decode=True)
                    if payload:
                        body = payload.decode(part.get_content_charset() or "utf-8", errors="ignore")
                        break
        else:
            payload = email_msg.get_payload(decode=True)
            if payload:
                body = payload.decode(email_msg.get_content_charset() or "utf-8", errors="ignore")

        return {
            "subject": subject,
            "sender": sender,
            "body": body.strip()
        }
    