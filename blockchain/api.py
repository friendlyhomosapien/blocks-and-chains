from flask import (Blueprint, jsonify, request, current_app)
from .blockchain import Blockchain
from .hashrate import calcHashRate

bp = Blueprint('api', __name__)

from blockchain.tasks import (
    getTransactions as get_transactions,
    startMining as start_mining,
    addTransaction as add_transaction,
    getChain as get_chain,
    validateChain as validate_chain
)

@bp.route('/transactions', methods=['GET'])
def getTransactions():
    current_app.logger.info('calling getTransactions')
    return get_transactions.delay().id


@bp.route('/transactions', methods=['POST'])
def addTransaction():
    jsonData = request.get_json()

    current_app.logger.info('calling addTransaction')

    if all(k in jsonData for k in ([
        'sender', 'receiver', 'amount', 'currency'
    ])):

        return add_transaction.delay(jsonData).id

    return jsonify({
        'error': 'Missing form data',
        'formData': jsonData
    }), 400


@bp.route('/hash-rate')
def hashRate():
    return calcHashRate(), 200


@bp.route('/mine', methods=['POST'])
def mine():
    current_app.logger.info('calling mine')

    return start_mining.delay().id


@bp.route('/chain', methods=['GET'])
def getChain():
    current_app.logger.info('calling getChain')

    return get_chain.delay().id


@bp.route('/chain/validate', methods=['POST'])
def chainValidate():
    return validate_chain.delay().id
