"""
ramp_results package

Result codes and acknowledgment structures for the
Railway Management Protocol (RAMP).

This package is independent from message definitions and
contains only result semantics and acknowledgment objects.
"""

from ramp_results.categories import ResultCategory
from ramp_results.codes import ResultCode
from ramp_results.acknowledgment import Acknowledgment
