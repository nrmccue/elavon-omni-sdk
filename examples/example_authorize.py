"""
Example: Authorize a payment.
"""

from elavon_omni_sdk import ElavonClient

client = ElavonClient(
    api_key="YOUR_API_KEY",
    secret_key="YOUR_SECRET_KEY"
)

payload = {
    "amount": 1000,
    "currency": "USD",
    "card": {
        "number": "4111111111111111",
        "expiry_month": "12",
        "expiry_year": "2030",
        "cvv": "123"
    }
}

response = client.authorize_payment(payload)
print(response)