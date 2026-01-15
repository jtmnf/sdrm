"""
Result categories for RAMP acknowledgments.
"""

from enum import Enum


class ResultCategory(Enum):
    """
    High-level classification of RAMP result codes.
    """

    SUCCESS = 1
    CLIENT_ERROR = 2
    SERVER_ERROR = 3
    ACTION_REQUIRED = 4
    CUSTOM = 5
