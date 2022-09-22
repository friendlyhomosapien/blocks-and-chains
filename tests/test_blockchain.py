import unittest
import time

from freezegun import freeze_time
from blockchain.blockchain import Blockchain
from blockchain.block import Block


class TestBlockchain(unittest.TestCase):
    freeze_at = '2022-01-01'
    test_payload = {
        'sender': 'test_sender',
        'receiver': 'test_receiver',
        'amount': 999,
        'currency': 999,
    }

    def test_genesis_block(self):
        with freeze_time(self.freeze_at):
            factory = Blockchain()

            factory.createGenesisBlock()

            self.assertEqual(len(factory.chain), 1)

    def test_add_transaction(self):
        with freeze_time(self.freeze_at):
            factory = Blockchain()

            new_transaction = factory.addTransaction(
                payload=self.test_payload
            )

            self.assertEqual(
                new_transaction.hash,
                factory.unconfirmed_transactions[-1].hash
            )
            self.assertEqual(
                new_transaction.payload,
                factory.unconfirmed_transactions[-1].payload
            )
            self.assertEqual(new_transaction.timestamp, time.time())

    def test_mine(self):
        factory = Blockchain()
        factory.addTransaction(payload=self.test_payload)
        self.assertEqual(factory.mineNext(), True)

    def test_validate_chain(self):
        factory = Blockchain()
        factory.addTransaction(payload=self.test_payload)

        factory.mineNext()

        self.assertEqual(factory.validateChain(), True)

    def test_validate_chain_invalid(self):
        factory = Blockchain()
        factory.addTransaction(payload=self.test_payload)

        factory.mineNext()

        block = Block(0, [], '0', time.time(), 0)
        block.hash = ''
        factory.chain.append(block)

        self.assertEqual(factory.validateChain(), False)
