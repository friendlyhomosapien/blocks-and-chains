from freezegun import freeze_time
from blockchain import Blockchain
import time


def test_genesis_block():
    with freeze_time('2022-01-01'):
        BlockchainInstance = Blockchain()

        assert len(BlockchainInstance.chain) == 1

        block = BlockchainInstance.chain[0]

        assert block['previous_hash'] == '0'
        assert block['timestamp'] == time.time()
        assert block['payload']['user_name'] == ''
        assert block['payload']['vote'] == 0


def test_create_block():
    with freeze_time('2022-01-01'):
        BlockchainInstance = Blockchain()

        previous_block = BlockchainInstance.previousBlock()
        previous_block_hashed = BlockchainInstance.hash(previous_block)

        new_block = BlockchainInstance.createBlock(
            'test_name',
            1,
            previous_block_hashed
        )

        assert new_block['previous_hash'] == previous_block_hashed
        assert new_block['timestamp'] == time.time()
        assert new_block['payload']['user_name'] == 'test_name'
        assert new_block['payload']['vote'] == 1
