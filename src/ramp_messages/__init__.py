"""
ramp_messages package

Base abstractions for the Railway Management Protocol (RAMP) message layer.

This package defines the canonical message contract used by all RAMP message
types. Concrete messages (FHM, HM, DM, DCM, UM) must inherit from RampMessage
and implement the required properties and payload structure.

This module intentionally contains no transport logic, acknowledgments, or
result-code handling.
"""

from abc import ABC, abstractmethod
import json
import time


class RampMessage(ABC):
    """
    Abstract base class for all RAMP messages.

    This class defines the minimal interface and shared initialization logic
    required by every message exchanged in the RAMP protocol.

    Concrete message classes must implement:
    - msg_type: symbolic identifier of the message type
    - topic: publish/subscribe topic used for message routing
    - payload(): JSON-serializable message body
    """

    def __init__(self, lc_id: str):
        """
        Initialize a RAMP message.

        Parameters
        ----------
        lc_id : str
            Unique identifier of the Local Controller (LC) originating
            or targeted by the message.
        """
        self.lc_id = lc_id
        self.timestamp = int(time.time() * 1000)

    @property
    @abstractmethod
    def msg_type(self) -> str:
        """
        Return the symbolic message type identifier (e.g., FHM, HM, DM).

        Returns
        -------
        str
            Message type identifier.
        """
        pass

    @property
    @abstractmethod
    def topic(self) -> str:
        """
        Return the publish/subscribe topic for this message.

        Returns
        -------
        str
            Topic string used by the messaging backend.
        """
        pass

    @abstractmethod
    def payload(self) -> dict:
        """
        Build the JSON-serializable payload of the message.

        Returns
        -------
        dict
            Message payload conforming to the RAMP specification.
        """
        pass

    def to_json(self) -> str:
        """
        Serialize the message payload to a compact JSON string.

        Returns
        -------
        str
            JSON-encoded message payload.
        """
        return json.dumps(self.payload(), separators=(",", ":"))
