from dotenv import load_dotenv
import os

load_dotenv()  # Load from .env

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_APP_PASS = os.getenv("EMAIL_APP_PASS")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

EMAIL_FILTER = 'UNSEEN'

ACTIONS_FILE = 'actions_log.json'

ACTION_DELIMETER = 'BEGIN_ACTIONS'
ACTION_RESPONSE_FORMAT = 'UNIT=<unit_or_apartment_parsed_from_email>\nACTIONS=action1, action2'
