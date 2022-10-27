import time
import json
import random
import string
from multiprocessing import Pool
from blockchain import Blockchain


class Simulation():
    max_workers = 4
    charSet = [
        string.ascii_letters,
        string.digits,
        string.punctuation
    ]

    def __init__(self):
        self.pool = Pool(max_workers=self.max_workers)
        self.bc = Blockchain()
        self.start()

    def start(self):
        self.addTransactions()
        self.mine()

    def addTransactions(self):
        payload = self.createRandomPayload()
        self.bc.addTransaction(payload=payload)
        time.sleep(.5)
        self.addTransaction()

    def mine(self):
        self.bc.mineNext()

        print(json.dumps(format(self.bc.last().toDict())))

        time.sleep(.5)
        self.mine()

    def createRandomPayload(self):
        return {
            'sender': self.createRandomString(),
            'receiver': self.createRandomString(),
            'amount': self.createRandomString(),
            'currency': self.createRandomString()
        }

    def createRandomString(self):
        # choose from all lowercase letter
        randomCharSet = self.charSet[random.randrange(len(self.charSet) - 1)]

        return ''.join(
            random.choice(randomCharSet) for i in range(random.randrange(0, 255))
        )

Simulation()
