"""
Definition of RAMP result codes.

Each result code follows the C.MS.SS format defined in the protocol.
"""

from dataclasses import dataclass
from ramp_results.categories import ResultCategory


@dataclass(frozen=True)
class ResultCode:
    """
    Represents a single RAMP result code.
    """

    code: str
    category: ResultCategory
    description: str


# --- Success codes ---
GENERIC_SUCCESS = ResultCode(
    code="1.00.00",
    category=ResultCategory.SUCCESS,
    description="Operation completed successfully.",
)

CONNECTED = ResultCode(
    code="1.01.00",
    category=ResultCategory.SUCCESS,
    description="Connection established successfully.",
)

HEARTBEAT_OK = ResultCode(
    code="1.06.00",
    category=ResultCategory.SUCCESS,
    description="Heartbeat received and accepted.",
)

# --- Client error codes ---
MALFORMED_MESSAGE = ResultCode(
    code="2.01.00",
    category=ResultCategory.CLIENT_ERROR,
    description="Message structure invalid or incomplete.",
)

UNKNOWN_TYPE = ResultCode(
    code="2.01.01",
    category=ResultCategory.CLIENT_ERROR,
    description="Message type not recognized.",
)
