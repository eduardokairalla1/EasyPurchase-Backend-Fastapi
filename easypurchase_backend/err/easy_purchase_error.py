"""
Base EasyPurchase error.
"""

# --- TYPES ---
from typing import Any


# --- GLOBAL ---
DEFAULT_MESSAGE = 'Generic EasyPurchase error'


# --- ERROR CLASS ---
class EasyPurchaseError(Exception):
    """
    Base EasyPurchase error.
    """
    message = DEFAULT_MESSAGE

    def __init__(self, *args: Any) -> None:
        """
        Initialize a EasyPurchase error.

        :param *args: Optional additional context or details for the error.

        :returns: None.
        """
        super().__init__(self.message, *args)
