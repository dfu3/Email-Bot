from email_client import EmailClient
from message_processor import MessageProcessor
from responder import Responder
from action_items import ActionItemGenerator
from datetime import datetime
import os
import json
from pprint import pprint as pp

ACTIONS_FILE = "actions_log.json"

def save_actions_to_file(email_data, unit, actions):
    timestamp = datetime.now().isoformat()
    entry = {
        "timestamp": timestamp,
        "email_subject": email_data["subject"],
        "email_sender": email_data["sender"],
        "actions": actions,
        "unit": unit
    }

    # Load existing entries if file exists
    if os.path.exists(ACTIONS_FILE):
        with open(ACTIONS_FILE, "r") as f:
            try:
                existing = json.load(f)
            except json.JSONDecodeError:
                existing = []
    else:
        existing = []

    existing.append(entry)

    # Write updated list
    with open(ACTIONS_FILE, "w") as f:
        json.dump(existing, f, indent=2)

def main():
    email_client = EmailClient()
    processor = MessageProcessor()
    responder = Responder()
    action_gen = ActionItemGenerator()

    messages = email_client.fetch_unread_messages()
    for msg in messages:
        parsed_email = processor.parse_email(msg)
        reply_raw = responder.generate_reply(parsed_email)
        reply, action_data = responder.clean_reply(reply_raw)
        pp(action_data)
        unit, actions = responder.parse_unit_and_actions(action_data)

        pp(f"\nReply:\n{reply}\n")
        pp(f"Action Items for Unit {unit}:\n{actions}\n")

        save_actions_to_file(parsed_email, unit, actions)
        email_client.send_reply(parsed_email, reply)

if __name__ == "__main__":
    main()
