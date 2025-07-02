"""
Example: Load API keys from .env environment variables.
"""

from elavon_omni_sdk import ElavonClient
from dotenv import load_dotenv
import os

load_dotenv()

client = ElavonClient(
    api_key=os.getenv("ELAVON_API_KEY"),
    secret_key=os.getenv("ELAVON_SECRET_KEY")
)

payload = {"amount": 1000, "currency": "USD"}
response = client.authorize_payment(payload)
print(response)