from enum import IntEnum


class ReturnCode(IntEnum):
    SUCCESS = 0
    BOOTSTRAP_FAILURE = 1
    NETWORK_FAILURE = 2
    MISSING_RANDOM = 3
    INVALID_KEY = 4
