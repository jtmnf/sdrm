"""
Definition of RAMP result codes.

Each result code follows the C.MS.SS format defined in the protocol.
"""

from dataclasses import dataclass
from ramp_results.categories import ResultCategory

# Current schema version for RAMP Result Codes
VERSION = "1.0.0"


def is_compatible(remote_version: str) -> bool:
    """
    Check if a remote version is compatible with the local schema.

    RAMP uses Semantic Versioning (Major.Minor.Patch).
    - Major versions must match.
    - Minor versions must be compatible (local >= remote generally,
      but for result codes, we typically require strict Major.Minor equality
      to ensure all codes are understood).

    For this implementation, we enforce that Major and Minor components match.
    Patch differences are allowed.

    Parameters
    ----------
    remote_version : str
        The version string received from the external system (e.g., "1.0.1").

    Returns
    -------
    bool
        True if compatible, False otherwise.
    """
    try:
        local_parts = VERSION.split(".")
        remote_parts = remote_version.split(".")

        # Ensure valid format
        if len(local_parts) != 3 or len(remote_parts) != 3:
            return False

        # Major check: Must match
        if local_parts[0] != remote_parts[0]:
            return False

        # Minor check: Must match (to ensure semantic understanding of all codes)
        if local_parts[1] != remote_parts[1]:
            return False

        # Patch check: Ignored (bug fixes don't change interface)
        return True

    except (AttributeError, ValueError):
        return False


@dataclass(frozen=True)
class ResultCode:
    """
    Represents a single RAMP result code.
    """

    code: str
    category: ResultCategory
    description: str


# --- Category 1: Success ---
GENERIC_SUCCESS = ResultCode(
    code="1.00.00",
    category=ResultCategory.SUCCESS,
    description="Operation completed successfully.",
)

ACKNOWLEDGED = ResultCode(
    code="1.00.01",
    category=ResultCategory.SUCCESS,
    description="Message acknowledged; no further action needed.",
)

ACCEPTED = ResultCode(
    code="1.00.02",
    category=ResultCategory.SUCCESS,
    description="Instruction accepted for processing.",
)

CONNECTED = ResultCode(
    code="1.01.00",
    category=ResultCategory.SUCCESS,
    description="Connection established successfully.",
)

RECONNECTED = ResultCode(
    code="1.01.01",
    category=ResultCategory.SUCCESS,
    description="Reconnection succeeded after temporary loss.",
)

DATA_STORED = ResultCode(
    code="1.03.00",
    category=ResultCategory.SUCCESS,
    description="Sensor data written to database.",
)

DATA_UPDATED = ResultCode(
    code="1.03.01",
    category=ResultCategory.SUCCESS,
    description="Existing record modified with new data.",
)

BATCH_STORED = ResultCode(
    code="1.03.02",
    category=ResultCategory.SUCCESS,
    description="Multiple data entries processed successfully.",
)

CONFIG_APPLIED = ResultCode(
    code="1.04.00",
    category=ResultCategory.SUCCESS,
    description="New configuration applied without errors.",
)

CONFIG_VALIDATED = ResultCode(
    code="1.04.01",
    category=ResultCategory.SUCCESS,
    description="Configuration validated; awaiting confirmation.",
)

UPDATE_COMPLETE = ResultCode(
    code="1.05.00",
    category=ResultCategory.SUCCESS,
    description="Update operation finished successfully.",
)

PATCH_APPLIED = ResultCode(
    code="1.05.01",
    category=ResultCategory.SUCCESS,
    description="System patch executed and logged.",
)

HEARTBEAT_OK = ResultCode(
    code="1.06.00",
    category=ResultCategory.SUCCESS,
    description="Heartbeat received and accepted.",
)

HEARTBEAT_SYNCED = ResultCode(
    code="1.06.01",
    category=ResultCategory.SUCCESS,
    description="Heartbeat interval synchronized successfully.",
)

SELFCHECK_PASSED = ResultCode(
    code="1.07.00",
    category=ResultCategory.SUCCESS,
    description="System health check completed successfully.",
)

MONITORING_OK = ResultCode(
    code="1.07.01",
    category=ResultCategory.SUCCESS,
    description="Monitoring components verified operational.",
)

RECOVERY_OK = ResultCode(
    code="1.07.02",
    category=ResultCategory.SUCCESS,
    description="System resumed normal state after recovery.",
)

FIRMWARE_VALIDATED = ResultCode(
    code="1.08.00",
    category=ResultCategory.SUCCESS,
    description="Firmware version validated against baseline.",
)

FIRMWARE_APPLIED = ResultCode(
    code="1.08.01",
    category=ResultCategory.SUCCESS,
    description="Firmware image applied and checksum verified.",
)

FIRMWARE_COMMITTED = ResultCode(
    code="1.08.02",
    category=ResultCategory.SUCCESS,
    description="Firmware version confirmed as active.",
)

RULES_LOADED = ResultCode(
    code="1.09.00",
    category=ResultCategory.SUCCESS,
    description="Decision ruleset loaded successfully.",
)

RULES_VALIDATED = ResultCode(
    code="1.09.01",
    category=ResultCategory.SUCCESS,
    description="Ruleset passed syntax and scope validation.",
)

RULES_ENFORCED = ResultCode(
    code="1.09.02",
    category=ResultCategory.SUCCESS,
    description="Runtime logic enforced current rule set.",
)


# --- Category 2: Client Error ---
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

MISSING_FIELDS = ResultCode(
    code="2.01.02",
    category=ResultCategory.CLIENT_ERROR,
    description="Required field(s) missing from payload.",
)

INVALID_PAYLOAD = ResultCode(
    code="2.01.03",
    category=ResultCategory.CLIENT_ERROR,
    description="One or more payload fields are incorrect.",
)

FIELD_TYPE_ERROR = ResultCode(
    code="2.01.04",
    category=ResultCategory.CLIENT_ERROR,
    description="Type mismatch in a required field.",
)

UNEXPECTED_STRUCTURE = ResultCode(
    code="2.01.05",
    category=ResultCategory.CLIENT_ERROR,
    description="Nested field layout does not match schema.",
)

UNAUTHORIZED = ResultCode(
    code="2.02.00",
    category=ResultCategory.CLIENT_ERROR,
    description="Token or identity check failed.",
)

TOKEN_EXPIRED = ResultCode(
    code="2.02.01",
    category=ResultCategory.CLIENT_ERROR,
    description="Provided token is no longer valid.",
)

ROLE_FORBIDDEN = ResultCode(
    code="2.02.02",
    category=ResultCategory.CLIENT_ERROR,
    description="Operation not permitted for this LC.",
)

CONNECTION_REFUSED = ResultCode(
    code="2.03.00",
    category=ResultCategory.CLIENT_ERROR,
    description="MC rejected handshake or payload.",
)

DUPLICATE_CONNECT = ResultCode(
    code="2.03.01",
    category=ResultCategory.CLIENT_ERROR,
    description="LC attempted to connect multiple times.",
)

UPDATE_REJECTED = ResultCode(
    code="2.04.00",
    category=ResultCategory.CLIENT_ERROR,
    description="Configuration update disallowed.",
)

FORMAT_DEPRECATED = ResultCode(
    code="2.04.01",
    category=ResultCategory.CLIENT_ERROR,
    description="Message format is deprecated or unsupported.",
)

BAD_HEARTBEAT = ResultCode(
    code="2.05.00",
    category=ResultCategory.CLIENT_ERROR,
    description="Heartbeat frequency or content invalid.",
)

OUT_OF_SYNC = ResultCode(
    code="2.05.01",
    category=ResultCategory.CLIENT_ERROR,
    description="Timestamps or sequence numbers inconsistent.",
)

CONFIG_CONFLICT = ResultCode(
    code="2.06.00",
    category=ResultCategory.CLIENT_ERROR,
    description="Two conflicting parameters detected.",
)

REJECTED_POLICY = ResultCode(
    code="2.06.01",
    category=ResultCategory.CLIENT_ERROR,
    description="Submitted change violates controller policy.",
)

INVALID_TIMESTAMP = ResultCode(
    code="2.06.02",
    category=ResultCategory.CLIENT_ERROR,
    description="Message timestamp is out of logical bounds.",
)

SEQUENCE_MISMATCH = ResultCode(
    code="2.06.03",
    category=ResultCategory.CLIENT_ERROR,
    description="Sequence counter does not align with prior state.",
)

PATCH_MALFORMED = ResultCode(
    code="2.07.00",
    category=ResultCategory.CLIENT_ERROR,
    description="Update patch could not be parsed.",
)

PATCH_CONFLICT = ResultCode(
    code="2.07.01",
    category=ResultCategory.CLIENT_ERROR,
    description="Patch conflicts with existing instructions.",
)

UPDATE_UNSAFE = ResultCode(
    code="2.07.02",
    category=ResultCategory.CLIENT_ERROR,
    description="Patch would compromise runtime safety.",
)

MISSING_DEPENDENCY = ResultCode(
    code="2.08.00",
    category=ResultCategory.CLIENT_ERROR,
    description="Operation references undeclared dependency.",
)

ILLEGAL_OVERRIDE = ResultCode(
    code="2.08.01",
    category=ResultCategory.CLIENT_ERROR,
    description="Attempt to override protected configuration.",
)


# --- Category 3: Server/Internal Error ---
INTERNAL_EXCEPTION = ResultCode(
    code="3.10.00",
    category=ResultCategory.SERVER_ERROR,
    description="Uncaught exception in message processing.",
)

DB_WRITE_ERROR = ResultCode(
    code="3.10.01",
    category=ResultCategory.SERVER_ERROR,
    description="Database could not commit the data.",
)

TRANSACTION_TIMEOUT = ResultCode(
    code="3.10.02",
    category=ResultCategory.SERVER_ERROR,
    description="Data commit operation exceeded timeout.",
)

LOCK_CONFLICT = ResultCode(
    code="3.10.03",
    category=ResultCategory.SERVER_ERROR,
    description="Concurrency control failure.",
)

QUEUE_FULL = ResultCode(
    code="3.11.00",
    category=ResultCategory.SERVER_ERROR,
    description="Internal message queue is full.",
)

DISPATCHER_FAILURE = ResultCode(
    code="3.11.01",
    category=ResultCategory.SERVER_ERROR,
    description="Routing logic failed to assign handler.",
)

RETRY_EXHAUSTED = ResultCode(
    code="3.11.02",
    category=ResultCategory.SERVER_ERROR,
    description="System retried operation and failed.",
)

DOWNSTREAM_DOWN = ResultCode(
    code="3.12.00",
    category=ResultCategory.SERVER_ERROR,
    description="Downstream service unavailable.",
)

STORAGE_OFFLINE = ResultCode(
    code="3.12.01",
    category=ResultCategory.SERVER_ERROR,
    description="Data layer cannot be accessed.",
)

ANALYTICS_FAILED = ResultCode(
    code="3.12.02",
    category=ResultCategory.SERVER_ERROR,
    description="MC analytics module failed to respond.",
)

EMERGENCY_STOP = ResultCode(
    code="3.13.00",
    category=ResultCategory.SERVER_ERROR,
    description="Critical fault triggered shutdown.",
)

MODULE_CRASH = ResultCode(
    code="3.14.00",
    category=ResultCategory.SERVER_ERROR,
    description="Internal service module encountered a fatal error.",
)

RESOURCE_STARVATION = ResultCode(
    code="3.14.01",
    category=ResultCategory.SERVER_ERROR,
    description="System unable to allocate memory or threads.",
)

INCONSISTENT_STATE = ResultCode(
    code="3.14.02",
    category=ResultCategory.SERVER_ERROR,
    description="Controller entered invalid runtime state.",
)

WATCHDOG_TRIGGERED = ResultCode(
    code="3.14.03",
    category=ResultCategory.SERVER_ERROR,
    description="System watchdog forced fault recovery.",
)

OVERFLOW_FAULT = ResultCode(
    code="3.15.00",
    category=ResultCategory.SERVER_ERROR,
    description="Numerical overflow or out-of-range computation.",
)

DIVISION_ERROR = ResultCode(
    code="3.15.01",
    category=ResultCategory.SERVER_ERROR,
    description="Division by zero or undefined result.",
)

RANGE_VIOLATION = ResultCode(
    code="3.15.02",
    category=ResultCategory.SERVER_ERROR,
    description="Access attempted beyond defined limits.",
)

SANDBOX_BREACH = ResultCode(
    code="3.16.00",
    category=ResultCategory.SERVER_ERROR,
    description="Isolated process violated runtime boundaries.",
)

MESSAGE_LEAK = ResultCode(
    code="3.16.01",
    category=ResultCategory.SERVER_ERROR,
    description="Data from restricted scope exposed.",
)


# --- Category 4: Action Required ---
RECONFIGURATION_REQUIRED = ResultCode(
    code="4.20.00",
    category=ResultCategory.ACTION_REQUIRED,
    description="Operation cannot proceed without setting changes.",
)

RETRY_SUGGESTED = ResultCode(
    code="4.20.01",
    category=ResultCategory.ACTION_REQUIRED,
    description="Temporary issue; retry may succeed.",
)

INVALID_SCHEMA = ResultCode(
    code="4.20.02",
    category=ResultCategory.ACTION_REQUIRED,
    description="Controller must update message schema.",
)

SELF_TEST_NEEDED = ResultCode(
    code="4.21.00",
    category=ResultCategory.ACTION_REQUIRED,
    description="Self-check must be initiated by LC.",
)

CALIBRATION_NEEDED = ResultCode(
    code="4.21.01",
    category=ResultCategory.ACTION_REQUIRED,
    description="Sensor needs calibration input.",
)

RESET_REQUIRED = ResultCode(
    code="4.21.02",
    category=ResultCategory.ACTION_REQUIRED,
    description="System requires reboot or state clear.",
)

MANUAL_INTERVENTION = ResultCode(
    code="4.22.00",
    category=ResultCategory.ACTION_REQUIRED,
    description="Action cannot proceed without human review.",
)

UNSAFE_CONDITION = ResultCode(
    code="4.22.01",
    category=ResultCategory.ACTION_REQUIRED,
    description="Safety check failed; operation paused.",
)

DEPLOYMENT_CHANGE = ResultCode(
    code="4.22.02",
    category=ResultCategory.ACTION_REQUIRED,
    description="Deployment configuration must be updated.",
)

RESERVED_MODE = ResultCode(
    code="4.22.03",
    category=ResultCategory.ACTION_REQUIRED,
    description="LC in restricted/maintenance mode.",
)

MANUAL_REBOOT = ResultCode(
    code="4.23.00",
    category=ResultCategory.ACTION_REQUIRED,
    description="Operator must restart the system physically.",
)

REPLACE_COMPONENT = ResultCode(
    code="4.23.01",
    category=ResultCategory.ACTION_REQUIRED,
    description="Physical sensor or module replacement needed.",
)

CONFIRM_OVERRIDE = ResultCode(
    code="4.23.02",
    category=ResultCategory.ACTION_REQUIRED,
    description="Policy override must be manually accepted.",
)

AWAIT_SCHEDULING = ResultCode(
    code="4.24.00",
    category=ResultCategory.ACTION_REQUIRED,
    description="LC placed in pending state by MC.",
)

CERTIFICATE_UPDATE = ResultCode(
    code="4.24.01",
    category=ResultCategory.ACTION_REQUIRED,
    description="Security certificate is outdated.",
)

ROLE_CHANGE_PENDING = ResultCode(
    code="4.24.02",
    category=ResultCategory.ACTION_REQUIRED,
    description="LC role update awaiting activation.",
)

CONFLICT_ESCALATION = ResultCode(
    code="4.25.00",
    category=ResultCategory.ACTION_REQUIRED,
    description="Operational conflict requires MC arbitration.",
)

LOG_REVIEW_REQUIRED = ResultCode(
    code="4.25.01",
    category=ResultCategory.ACTION_REQUIRED,
    description="Event logs must be reviewed before continuation.",
)

ENTER_DEGRADED_MODE = ResultCode(
    code="4.25.02",
    category=ResultCategory.ACTION_REQUIRED,
    description="LC must reduce capability until resolved.",
)

GRACE_PERIOD_EXPIRED = ResultCode(
    code="4.25.03",
    category=ResultCategory.ACTION_REQUIRED,
    description="Required update window has elapsed.",
)


# --- Category 5: Vendor/Custom ---
CUSTOM_HANDLER = ResultCode(
    code="5.99.00",
    category=ResultCategory.CUSTOM,
    description="Message processed by custom integration logic.",
)