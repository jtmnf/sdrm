"""
Update Message (UM)

Implements runtime reconfiguration instructions sent from the
Main Controller to a Local Controller.
"""

from ramp_messages import RampMessage


class UpdateMessage(RampMessage):
    """
    Update Message (UM).

    Carries one or more configuration or control instructions to be
    applied by a Local Controller at runtime.
    """

    def __init__(self, lc_id: str, updates: list[dict]):
        """
        Initialize an Update Message.

        Parameters
        ----------
        lc_id : str
            Identifier of the target Local Controller.
        updates : list of dict
            List of update instructions.
        """
        super().__init__(lc_id)
        self.updates = updates

    @property
    def msg_type(self) -> str:
        """Return the message type identifier."""
        return "UM"

    @property
    def topic(self) -> str:
        """Return the update topic."""
        return f"/lc/{self.lc_id}/update/"

    def payload(self) -> dict:
        """
        Build the update message payload.

        Returns
        -------
        dict
            Update message payload.
        """
        return self.updates
