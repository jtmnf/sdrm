"""
Acknowledgment object for RAMP messages.
"""

import time
from ramp_results.codes import ResultCode


class Acknowledgment:
    """
    Represents a RAMP acknowledgment message.

    This object reports the outcome of processing a RAMP message
    using a structured result code.
    """

    def __init__(
        self,
        result: ResultCode,
        msg_type: str,
        original_ts: int,
        version: str = "1.0.0",
    ):
        """
        Initialize an acknowledgment.

        Parameters
        ----------
        result : ResultCode
            Result of the processed operation.
        msg_type : str
            Type of the original message being acknowledged.
        original_ts : int
            Timestamp of the original message (epoch ms).
        version : str
            Result table version.
        """
        self.result = result
        self.msg_type = msg_type
        self.original_ts = original_ts
        self.version = version
        self.ack_ts = int(time.time() * 1000)

    def payload(self) -> dict:
        """
        Build the acknowledgment payload.

        Returns
        -------
        dict
            JSON-serializable acknowledgment payload.
        """
        return {
            "result": self.result.code,
            "version": self.version,
            "msg_type": self.msg_type,
            "original_ts": self.original_ts,
            "ack_ts": self.ack_ts,
        }
