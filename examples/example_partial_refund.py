"""
Example: Refund part of a payment.
"""

from elavon_omni_sdk import ElavonClient

client = ElavonClient(
    api_key="YOUR_API_KEY",
    secret_key="YOUR_SECRET_KEY"
)

transaction_id = "capture_txn_456"

response = client.refund_payment(transaction_id, amount=500)
print(response)