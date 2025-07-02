"""
Example: Use a different API version (v2).
"""

from elavon_omni_sdk import ElavonClient

client = ElavonClient(
    api_key="YOUR_API_KEY",
    secret_key="YOUR_SECRET_KEY",
    api_version="v2"
)

payload = {"amount": 1000, "currency": "USD"}
response = client.authorize_payment(payload)
print(response)
