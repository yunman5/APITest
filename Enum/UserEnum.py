from enum import Enum


class UserType(Enum):
    staff = 0
    visitor = 1
    vendor = 2
    tenant = 3


class EnableState(Enum):
    enabled = 0
    disabled = 1
    expired = 2
    inactive = 2

class Status(Enum):
    Enabled = 0
    Disabled = 1
    Expired = 2
    Inactive = 3

class validityType(Enum):
    Permanent = 0
    Customize = 1


class accessRule(Enum):
    SingleEntry = 0
    MultipleEntry = 1
