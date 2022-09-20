import unittest
import time

from freezegun import freeze_time
from src.Blockchain import Blockchain


class TestBlockchain(unittest.TestCase):
    def test_create_block(self):
        with freeze_time('2022-01-01'):
            factory = Blockchain()

            new_block = factory.addTransaction(
                jsonData={
                    'sender': 'test_sender',
                    'receiver': 'test_receiver',
                    'amount': 999,
                    'currency': 999,
                }
            )

            self.assertEqual(new_block.hash(), factory.lastHash())
            self.assertEqual(new_block.timestamp, time.time())

    def test_genesis_block(self):
        with freeze_time('2022-01-01'):
            factory = Blockchain()

            self.assertEqual(len(factory.chain), 1)

            block = factory.chain[0]

            self.assertEqual(block['previous_hash'], '0')
            self.assertEqual(block['timestamp'], time.time())
