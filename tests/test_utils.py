"""
Tests for utility functions.
"""

from elavon_omni_sdk.utils import generate_signature

def test_generate_signature():
    signature = generate_signature("secret", "message")
    assert isinstance(signature, str)