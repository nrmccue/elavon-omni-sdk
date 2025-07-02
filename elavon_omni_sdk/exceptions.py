"""
Custom exception classes for SDK errors.
"""

class ElavonSDKError(Exception):
    """Base class for all SDK exceptions."""
    pass

class AuthenticationError(ElavonSDKError):
    """Raised when authentication fails."""
    pass

class APIRequestError(ElavonSDKError):
    """Raised when the API request fails."""
    pass