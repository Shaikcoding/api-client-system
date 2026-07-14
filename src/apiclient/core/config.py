from pydantic import BaseModel
from typing import Optional

class TimeoutConfig(BaseModel):
    connect: float = 5.0
    read: float = 30.0
    write: float = 10.0

class ClientConfig(BaseModel):
    base_url: str
    api_key: Optional[str] = None
    timeout: TimeoutConfig = TimeoutConfig()