from blockchain import celery
from blockchain.blockchain import Blockchain

blockchain = Blockchain()
blockchain.createGenesisBlock()


@celery.task
def getTransactions():
    return blockchain.getUnconfirmedTransactions()


@celery.task
def startMining():
    return blockchain.mineNext()


@celery.task
def addTransaction(payload):
    return blockchain.addTransaction(payload)


@celery.task
def getChain():
    return blockchain.getChain()


@celery.task
def validateChain():
    return blockchain.validateChain()
