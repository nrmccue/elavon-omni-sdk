"""
Tests for custom exceptions.
"""

from elavon_omni_sdk.exceptions import AuthenticationError

def test_authentication_error():
    try:
        raise AuthenticationError("Auth failed")
    except AuthenticationError as e:
        assert str(e) == "Auth failed"