"""
Example: Capture a previously authorized payment.
"""

from elavon_omni_sdk import ElavonClient

client = ElavonClient(
    api_key="YOUR_API_KEY",
    secret_key="YOUR_SECRET_KEY"
)

transaction_id = "auth_txn_123"

response = client.capture_payment(transaction_id, amount=1000)
print(response)