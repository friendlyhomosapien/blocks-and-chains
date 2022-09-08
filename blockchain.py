import hashlib
import time
import json


class Blockchain:
    def __init__(self):
        self.chain = []
        self.createBlock(user_name='', vote=0, previous_hash='0')

    def createBlock(self, user_name, vote, previous_hash):
        block = {
            'payload': {
                'user_name': user_name,
                'vote': vote,
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
