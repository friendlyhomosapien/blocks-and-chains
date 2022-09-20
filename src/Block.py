from hashlib import sha256
import json
import time


class Block():
    def __init__(
        self,
        proof,
        previous_hash,
        timestamp,
        payload
    ) -> None:
        self.timestamp = timestamp

        self.previous_hash = previous_hash

        self.proof = proof

        self.payload = payload

        self.time_confirmed = time.time()

    def hash(self):
        block_string = json.dumps(self.__dict__, sort_keys=True).encode()
        return sha256(block_string).hexdigest()

