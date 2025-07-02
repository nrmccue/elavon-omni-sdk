"""
ElavonClient class - handles API requests to Elavon
"""

class ElavonClient:
    def __init__(self, api_key, secret_key, api_version="v1"):
        """
        Initialize the client with credentials and version.
        """
        self.api_key = api_key
        self.secret_key = secret_key
        self.api_version = api_version

    def authorize_payment(self, payload):
        """
        Authorize a payment.
        """
        pass

    def capture_payment(self, transaction_id, amount):
        """
        Capture a previously authorized payment.
        """
        pass

    def refund_payment(self, transaction_id, amount):
        """
        Refund a payment.
        """
        pass