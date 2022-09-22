import json
from multiprocessing import Pool

from .block import Block
from .transaction import Transaction


class Blockchain:
    difficulty = 1
    max_workers = 4
    pool = None
    batch_size = int(2.5e5)
    unconfirmed_transactions = []

    def __init__(self) -> None:
        self.chain = []
        self.mempool = []
        self.unconfirmed_transactions = []

    def __str__(self):
        return json.dumps(self.getChain(), ensure_ascii=False)

    def getChain(self):
        return [block.toDict() for block in self.chain]

    def getUnconfirmedTransactions(self):
        return [
            transaction.toDict() for transaction
            in self.unconfirmed_transactions
        ]

    def last(self):
        return self.chain[-1]

    def createGenesisBlock(self) -> Block:
        genesis_block = Block(0, [Transaction('genesis')], '0', None, 0)

        genesis_block.nonce, genesis_block.hash = self.mine(genesis_block)

        self.chain.append(genesis_block)

        return genesis_block

    def validateProof(self, block: Block, proof: str) -> bool:
        return (
            proof.startswith('0' * Blockchain.difficulty) and
            proof == block.createHash()
        )

    def validateChain(self) -> bool:
        is_valid = True
        prev_hash = '0'

        for block in self.chain:
            proof = block.createHash()
            delattr(block, 'hash')

            print(prev_hash)
            print(block.previous_hash)

            if (
                not self.validateProof(block, proof)
                or prev_hash != block.previous_hash
            ):
                is_valid = False
                break

            block.hash, prev_hash = proof, proof

        return is_valid

    def createProof(block: Block, start_nonce: int, end_nonce: int):
        block.nonce = start_nonce

        hash = ''

        print('Searched from %d to %d' % (start_nonce, end_nonce))

        for nonce in range(start_nonce, end_nonce):
            block.nonce = nonce
            hash = block.createHash()
            if hash.startswith('0' * Blockchain.difficulty):
                return (nonce, hash)

        return None

    def addTransaction(self, payload):
        if len(self.unconfirmed_transactions) == 0 and len(self.chain) == 0:
            self.createGenesisBlock()

        transaction = Transaction(payload)

        self.unconfirmed_transactions.append(transaction)

        return transaction

    def startProcess(args) -> tuple:
        block, nonce_range = args
        return Blockchain.createProof(block, nonce_range[0], nonce_range[1])

    def mine(self, block: Block) -> tuple:
        pool = Pool(processes=Blockchain.max_workers)

        nonce = 0

        while True:
            nonce_ranges = [
                (nonce + i * self.batch_size, nonce + (i+1) * self.batch_size)
                for i in range(self.max_workers)
            ]

            params = [
                (block, nonce_range) for nonce_range in nonce_ranges
            ]

            for result in pool.imap_unordered(
                Blockchain.startProcess,
                params
            ):
                if result is not None:
                    # Remove unconfirmed transactions
                    self.unconfirmed_transactions = []
                    pool.close()
                    return result

            nonce += self.max_workers * self.batch_size

    def addBlock(self, block: Block, proof: str) -> bool:
        if (
            self.last().createHash() != block.previous_hash
            and len(self.chain) > 1
        ):
            print('last block hash does not match block previous hash')
            return False

        if not self.validateProof(block, proof):
            print('invalid proof')
            return False

        block.hash = proof

        self.chain.append(block)

        return True

    def mineNext(self) -> bool:
        if not self.unconfirmed_transactions:
            return False

        next_block = Block(
            self.last().index + 1,
            self.unconfirmed_transactions,
            self.last().createHash()
        )

        next_block.nonce, proof = self.mine(next_block)

        return self.addBlock(next_block, proof)
