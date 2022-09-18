import hashlib
import time
import json


class Blockchain:
    def __init__(self):
        self.chain = []
        self.createBlock(
            sender_name='',
            amount=0,
            currency='none',
            previous_hash='0'
        )

    def createBlock(self, sender_name, amount, currency, previous_hash):
        block = {
            'payload': {
                'sender_name': sender_name,
                'amount': amount,
                'currency': currency
            },
            'previous_hash': previous_hash,
            'timestamp': time.time()
        }
        self.chain.append(block)
        return block

    def previousBlock(self):
        return self.chain[-1]

    def hash(self, block):
        encoded_block = json.dumps(block).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    def fields(self):
        return [
            'sender_name',
            'amount',
            'currency',
        ]
