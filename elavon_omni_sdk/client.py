"""
ElavonClient class - handles API requests to Elavon Omni Commerce Gateway
"""

import requests
import time
import hmac
import hashlib
from .config import API_VERSIONS, SANDBOX_API_VERSIONS, DEFAULT_TIMEOUT
from .exceptions import AuthenticationError, APIRequestError

class ElavonClient:
    def __init__(self, api_key, secret_key, api_version="v1", environment="sandbox"):
        """
        Initialize the client with credentials and settings.
        """
        self.api_key = api_key
        self.secret_key = secret_key
        self.api_version = api_version
        self.environment = environment

        # Pick correct base URL based on environment
        if self.environment == "sandbox":
            self.base_url = SANDBOX_API_VERSIONS.get(api_version)
        else:
            self.base_url = API_VERSIONS.get(api_version)

        if not self.base_url:
            raise ValueError(f"Unsupported API version: {api_version}")

    def _generate_signature(self, message):
        """
        Generate HMAC SHA256 signature.
        """
        return hmac.new(
            key=self.secret_key.encode("utf-8"),
            msg=message.encode("utf-8"),
            digestmod=hashlib.sha256
        ).hexdigest()

    def _request(self, method, path, payload=None):
        """
        Internal helper to send HTTP requests to Elavon API.
        """
        url = f"{self.base_url}{path}"

        timestamp = str(int(time.time()))
        body = payload if payload else {}

        message = f"{timestamp}{method.upper()}{path}{body}"
        signature = self._generate_signature(message)

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"HMAC {self.api_key}:{signature}",
            "Timestamp": timestamp
        }

        try:
            response = requests.request(
                method=method,
                url=url,
                json=body,
                headers=headers,
                timeout=DEFAULT_TIMEOUT
            )
        except requests.exceptions.RequestException as e:
            raise APIRequestError(f"Network error: {str(e)}")

        if response.status_code == 401:
            raise AuthenticationError("Invalid API credentials.")
        elif not response.ok:
            raise APIRequestError(f"API error: {response.status_code} {response.text}")

        return response.json()

    def authorize_payment(self, payload):
        """
        Authorize a payment.
        """
        return self._request("POST", "payments/authorize", payload)

    def capture_payment(self, transaction_id, amount):
        """
        Capture a previously authorized payment.
        """
        payload = {"amount": amount}
        return self._request("POST", f"payments/{transaction_id}/capture", payload)

    def refund_payment(self, transaction_id, amount):
        """
        Refund a payment.
        """
        payload = {"amount": amount}
        return self._request("POST", f"payments/{transaction_id}/refund", payload)

    def void_authorization(self, transaction_id):
        """
        Void an authorization.
        """
        return self._request("POST", f"payments/{transaction_id}/void")

    def get_transaction(self, transaction_id):
        """
        Retrieve transaction details.
        """
        return self._request("GET", f"payments/{transaction_id}")