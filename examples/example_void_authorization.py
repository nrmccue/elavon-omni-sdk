"""
Example: Void an authorization before capture.
"""

from elavon_omni_sdk import ElavonClient

client = ElavonClient(
    api_key="YOUR_API_KEY",
    secret_key="YOUR_SECRET_KEY"
)

transaction_id = "auth_txn_789"

response = client.void_authorization(transaction_id)
print(response)