from dotenv import load_dotenv
import os

load_dotenv()  # Load from .env

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_APP_PASS = os.getenv("EMAIL_APP_PASS")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
