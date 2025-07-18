import json

class ActionItemGenerator:
    def generate_actions(self, email_data):
        actions = []

        body = email_data["body"].lower()
        if "toilet" in body or "leak" in body or "broken" in body:
            actions.append({"type": "maintenance", "issue": "reported issue", "address": "parsed from email"})

        if "locked out" in body:
            actions.append({"type": "access", "note": "Tenant locked out"})

        return json.dumps(actions, indent=2)
