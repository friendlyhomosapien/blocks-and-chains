from hashlib import sha256
from .Blockchain import Blockchain
from .Block import Block


BlockchainInstance = Blockchain()


class Pool():
    def __init__(self):
        self.mempool = []
