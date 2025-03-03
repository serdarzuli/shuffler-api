import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

BASE_URL = "https://shuffler.io/api/v1"

CERT_PATH = os.getenv("CERT_PATH")
KEY_PATH = os.getenv("KEY_PATH")
TOKEN = os.getenv("API_TOKEN")
