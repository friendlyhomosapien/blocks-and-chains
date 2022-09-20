import time


class Transaction():
    def __init__(
        self,
        payload
    ):
        self.proof = None
        self.timestamp = time.time()
        self.payload = payload\

    def payloadFields():
        return [
            'sender',
            'receiver',
            'amount',
            'currency',
        ]
