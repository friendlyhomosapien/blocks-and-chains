import time
from .Block import Block
from .Transaction import Transaction
from multiprocessing import Pool


def create_hash(x:int) -> str:
    block = Block(1, [Transaction('hello')], '0', '1234567890', x)

    return block.createHash()

def calcHashRate():
    max_hashes = 10000000
    max_workers = 4

    pool = Pool(processes=max_workers)

    start_time = time.time()

    pool.map(create_hash, range(max_hashes))

    end_time = time.time()   

    perf = (end_time - start_time, max_hashes)
    
    hash_rate = perf[1] / perf[0];

    print("Hashes per second: {}".format(hash_rate))
    print("Seconds passed: {}".format(end_time - start_time))

    return str(hash_rate)