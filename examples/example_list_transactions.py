"""
Example: List transactions with optional filters.
"""

from elavon_omni_sdk import ElavonClient

client = ElavonClient(
    api_key="YOUR_API_KEY",
    secret_key="YOUR_SECRET_KEY"
)

filters = {
    "status": "captured",
    "limit": 10
}

response = client.list_transactions(filters)
print(response)