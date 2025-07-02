"""
Helper functions for signature generation and timestamps.
"""

import hmac
import hashlib

def generate_signature(secret_key, message):
    """
    Generate HMAC SHA256 signature.
    """
    return hmac.new(
        key=secret_key.encode("utf-8"),
        msg=message.encode("utf-8"),
        digestmod=hashlib.sha256
    ).hexdigest()