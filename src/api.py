from flask import (Blueprint, jsonify, request)
from .Blockchain import Blockchain
from .Block import Block
from .Transaction import Transaction


bp = Blueprint('api', __name__)

BlockchainInstance = Blockchain()


@bp.route('/mine', methods=['POST'])
def mine():
    jsonData = request.get_json()

    if all(k in jsonData for k in (Transaction.payloadFields())):

        BlockchainInstance.addTransaction(jsonData)

        return jsonify(jsonData), 200

    return jsonify({
        'error': 'Missing form data',
        'formData': jsonData
    }), 400


@bp.route('/chain', methods=['GET'])
def chain():
    return jsonify(BlockchainInstance.chain), 200


@bp.route('/pool', methods=['GET'])
def pool():
    return jsonify(BlockchainInstance.mempool), 200
