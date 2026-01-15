"""
Heartbeat Message (HM)

Implements the periodic liveness signal sent by a Local Controller to
indicate continued availability.
"""

from ramp_messages import RampMessage


class HeartbeatMessage(RampMessage):
    """
    Heartbeat Message (HM).

    Periodically transmitted by a Local Controller to confirm that it is
    online and operational.
    """

    def __init__(self, lc_id: str, heartrate: int):
        """
        Initialize a Heartbeat Message.

        Parameters
        ----------
        lc_id : str
            Identifier of the Local Controller.
        heartrate : int
            Interval (in seconds) between heartbeat messages.
        """
        super().__init__(lc_id)
        self.heartrate = heartrate

    @property
    def msg_type(self) -> str:
        """Return the message type identifier."""
        return "HM"

    @property
    def topic(self) -> str:
        """Return the heartbeat topic."""
        return f"/lc/{self.lc_id}/heartbeat/"

    def payload(self) -> dict:
        """
        Build the heartbeat payload.

        Returns
        -------
        dict
            Heartbeat message payload.
        """
        return {
            "heartbeat": 1,
            "heartrate": self.heartrate,
        }
