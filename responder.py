from openai import OpenAI
from config import OPENAI_API_KEY
from pprint import pprint as pp

class Responder:
    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_API_KEY)

    def generate_reply(self, email_data):
        prompt = f"""Reply as a helpful property manager. Here's the email:
Subject: {email_data['subject']}
Body: {email_data['body']}"""
        
        pp(prompt)

        try:
            response = self.client.chat.completions.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=200
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            print("OpenAI error:", e)
            return "Sorry, we're reviewing your request and will get back shortly."
