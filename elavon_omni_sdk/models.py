"""
Data models for request and response objects.
"""

from dataclasses import dataclass

@dataclass
class PaymentResponse:
    transaction_id: str
    status: str
    amount: int