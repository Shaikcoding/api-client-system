import httpx
from .config import ClientConfig

class APIClient:
    def __init__(self, config: ClientConfig):
        self.config = config
        self._session = httpx.Client(
            base_url=config.base_url,
            timeout=config.timeout.connect
        )
    
    def get(self, path: str):
        response = self._session.get(path)
        response.raise_for_status()
        return response.json()
    
    def close(self):
        self._session.close()