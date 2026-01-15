"""
Disconnect Message (DCM)

Implements a graceful session termination request from a Local Controller.
"""

from ramp_messages import RampMessage


class DisconnectMessage(RampMessage):
    """
    Disconnect Message (DCM).

    Explicitly informs the Main Controller that the Local Controller
    intends to terminate the session.
    """

    @property
    def msg_type(self) -> str:
        """Return the message type identifier."""
        return "DCM"

    @property
    def topic(self) -> str:
        """Return the disconnect topic."""
        return f"/lc/{self.lc_id}/disconnect/"

    def payload(self) -> dict:
        """
        Build the disconnect payload.

        Returns
        -------
        dict
            Disconnect message payload.
        """
        return {"disconnect": 1}
