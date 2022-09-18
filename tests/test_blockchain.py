import unittest
import time

from freezegun import freeze_time
from src.blockchain import Blockchain

class TestBlockchain(unittest.TestCase):
    def test_create_block(self):
        with freeze_time('2022-01-01'):
            BlockchainInstance = Blockchain()

            previous_block = BlockchainInstance.previousBlock()
            previous_block_hashed = BlockchainInstance.hash(previous_block)

            new_block = BlockchainInstance.createBlock(
                'test_user',
                999,
                'USD',
                previous_block_hashed
            )

            self.assertEqual(new_block['previous_hash'], previous_block_hashed)
            self.assertEqual(new_block['timestamp'], time.time())
            self.assertEqual(new_block['payload']['sender_name'], 'test_user')
            self.assertEqual(new_block['payload']['amount'], 999)
            self.assertEqual(new_block['payload']['currency'], 'USD')

    def test_genesis_block(self):
        with freeze_time('2022-01-01'):
            BlockchainInstance = Blockchain()

            assert len(BlockchainInstance.chain) == 1

            block = BlockchainInstance.chain[0]

            self.assertEqual(block['previous_hash'], '0')
            self.assertEqual(block['timestamp'], time.time())
            self.assertEqual(block['payload']['sender_name'], '')
            self.assertEqual(block['payload']['amount'], 0)
            self.assertEqual(block['payload']['currency'], 'none')
