from datetime import datetime
from config import ACTIONS_FILE
import json
import os

class ActionManager():

    def __init__(self):
        if os.path.exists(ACTIONS_FILE):
            with open(ACTIONS_FILE, "r") as f:
                try:
                    existing = json.load(f)
                except json.JSONDecodeError:
                    existing = []
        else:
            existing = []
        self.action_log = existing

    def process_and_save(self, email_data, unit, actions):
        timestamp = datetime.now().isoformat()
        entry = {
            "timestamp": timestamp,
            "email_subject": email_data["subject"],
            "email_sender": email_data["sender"],
            "actions": actions,
            "unit": unit
        }

        # TODO
        # check for actions that can be automated and generate followup com
        # ex: how much is my rent -> lookup unit from data_store and send result in email
        # then remove them from the list before adding to the log

        self.action_log.append(entry)

        with open(ACTIONS_FILE, "w") as f:
            json.dump(self.action_log, f, indent=2)