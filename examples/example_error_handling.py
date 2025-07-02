"""
Example: Handling errors gracefully.
"""

from elavon_omni_sdk import ElavonClient
from elavon_omni_sdk.exceptions import APIRequestError, AuthenticationError

client = ElavonClient(
    api_key="INVALID_KEY",
    secret_key="INVALID_SECRET"
)

try:
    payload = {"amount": 1000, "currency": "USD"}
    response = client.authorize_payment(payload)
    print(response)
except AuthenticationError as e:
    print("Authentication failed:", e)
except APIRequestError as e:
    print("API request error:", e)