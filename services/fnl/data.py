from dataclasses import dataclass
from datetime import datetime

@dataclass(frozen=True)
class FNLFile:
    time: datetime
    url: str
    filename: str
    exists: bool