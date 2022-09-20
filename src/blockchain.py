import json
import time
from hashlib import sha256

from .Block import Block
from .Transaction import Transaction


class Blockchain:
    def __init__(self) -> None:
        self.chain = []
        self.mempool = []
        block = Block(
            proof=1,
            previous_hash='0',
            timestamp=time.time(),
            payload={
                'sender': '',
                'receiver': '',
                'amount': 0,
                'currency': 'none'
            }
        )

        self.chain.append(block.__dict__)

    def last(self):
        return self.chain[-1]

    def lastHash(self) -> str:
        return self.hash(self.last())

    def hash(self, block):
        block_string = json.dumps(block, sort_keys=True).encode()
        return sha256(block_string).hexdigest()

    def proof(self, previous_proof):
        proof = 1
        check_proof = False

        while check_proof is False:
            hash_operation = sha256(
                str(proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:5] == '00000':
                check_proof = True
            else:
                proof += 1

        return proof

    def addTransaction(self, jsonData: dict):
        transaction = Transaction(payload=jsonData).__dict__

        self.mempool.append(transaction)

        transaction['proof'] = self.proof(self.chain[-1]['proof'])
        transaction['previous_hash'] = self.lastHash()

        self.mempool.pop(0)

        block = Block(
            proof=transaction['proof'],
            previous_hash=transaction['previous_hash'],
            timestamp=transaction['timestamp'],
            payload=transaction['payload']
        )

        self.chain.append(block.__dict__)

        return block
