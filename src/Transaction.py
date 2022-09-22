import time
import json
from hashlib import sha256


class Transaction():
    def __init__(
        self,
        payload={}
    ) -> None:
        self.payload = payload
        self.timestamp = int(time.time())
        self.hash = self.createHash()

    def createHash(self) -> str:
        return sha256(sha256('{}{}'.format(self.payload, self.timestamp).encode()).hexdigest().encode('utf8')).hexdigest()

    def toDict(self) -> dict:
        return dict(
            payload=self.payload,
            timestamp=self.timestamp,
            hash=self.hash
        )
