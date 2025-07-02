from elavon_omni_sdk import ElavonClient
from dotenv import load_dotenv
import os

# Load your environment variables from .env
load_dotenv()

api_key = os.getenv("ELAVON_API_KEY")
secret_key = os.getenv("ELAVON_SECRET_KEY")
environment = os.getenv("ENVIRONMENT", "sandbox")

# Create the client
client = ElavonClient(
    api_key=api_key,
    secret_key=secret_key,
    api_version="v1",
    environment=environment
)

# ✅ This is your valid JSON payload
payload = {
    "transaction_type": "ccauthonly",
    "amount": "1.00",
    "card_number": "4111111111111111",
    "card_expiry": "1225",
    "card_cvv": "123"
}

# Send the request
try:
    response = client.authorize_payment(payload)
    print("Success:", response)
except Exception as e:
    print("Error:", e)