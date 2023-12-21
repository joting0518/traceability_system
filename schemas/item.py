# schemas/order.py
from enum import Enum

class ItemStatus(str, Enum):
    SAMPLING = "sampling"
    NOSAMPLING = "no_sampling"
    WAITSAMPLING = "wait_sampling"
    UNKNOWN = "unknown"

class ItemInspector(str, Enum):
    ANDY = "Andy"
    ALICE = "Alice"


