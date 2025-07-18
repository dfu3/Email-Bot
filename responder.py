from openai import OpenAI
from config import OPENAI_API_KEY
from pprint import pprint as pp
from config import ACTION_DELIMETER, ACTION_RESPONSE_FORMAT

class Responder:
    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_API_KEY)

    def parse_unit_and_actions(self, action_data):
        unit = ""
        actions = []

        for line in action_data.strip().splitlines():
            if line.startswith("UNIT="):
                unit = line[len("UNIT="):].strip()
            elif line.startswith("ACTIONS="):
                actions = [a.strip() for a in line[len("ACTIONS="):].split(",") if a.strip()]

        return unit, actions
    
    def clean_reply(self, reply_raw):
        if not reply_raw.find(ACTION_DELIMETER):
            return (reply_raw, "")
        
        return reply_raw.split(ACTION_DELIMETER)

    def generate_reply(self, email_data):
        prompt = f"""Reply as a helpful property manager. Sign off as 'Property Manager'.
            After the reply, 
            separately list any action items using this format exactly:
            {ACTION_DELIMETER}
            {ACTION_RESPONSE_FORMAT}
            Here's the email:
            Subject: {email_data['subject']}
            Body: {email_data['body']}"""
        
        # pp(prompt)

        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=200
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            print("OpenAI error:", e)
            return "Sorry, we're reviewing your request and will get back shortly."
