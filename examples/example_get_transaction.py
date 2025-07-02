"""
Example: Retrieve details of a transaction.
"""

from elavon_omni_sdk import ElavonClient

client = ElavonClient(
    api_key="YOUR_API_KEY",
    secret_key="YOUR_SECRET_KEY"
)

transaction_id = "any_txn_001"

response = client.get_transaction(transaction_id)
print(response)