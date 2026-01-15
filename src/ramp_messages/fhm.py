"""
First Handshake Message (FHM)

Implements the initial connection message sent by a Local Controller (LC)
to a Main Controller (MC) to establish a RAMP session.
"""

from ramp_messages import RampMessage


class FirstHandshakeMessage(RampMessage):
    """
    First Handshake Message (FHM).

    This message registers a Local Controller with the Main Controller and
    optionally advertises attached sensors and train metadata.
    """

    def __init__(
            self,
            lc_id: str,
            name: str,
            ip: str,
            train_id: int | None = None,
            sensors: list[dict] | None = None,
    ):
        """
        Initialize a First Handshake Message.

        Parameters
        ----------
        lc_id : str
            Unique identifier of the Local Controller.
        name : str
            Human-readable name of the Local Controller.
        ip : str
            IP address or hostname of the Local Controller.
        train_id : int, optional
            Identifier of the associated train.
        sensors : list of dict, optional
            List of sensor descriptors attached to the controller.
        """
        super().__init__(lc_id)
        self.name = name
        self.ip = ip
        self.train_id = train_id
        self.sensors = sensors or []

    @property
    def msg_type(self) -> str:
        """Return the message type identifier."""
        return "FHM"

    @property
    def topic(self) -> str:
        """Return the handshake request topic."""
        return f"/mc/{self.lc_id}/new_connection/request"

    def payload(self) -> dict:
        """
        Build the FHM payload.

        Returns
        -------
        dict
            Handshake message payload.
        """
        data = {
            "id": self.lc_id,
            "name": self.name,
            "ip": self.ip,
        }
        if self.train_id is not None:
            data["train_id"] = self.train_id
        if self.sensors:
            data["sensors"] = self.sensors
        return data
