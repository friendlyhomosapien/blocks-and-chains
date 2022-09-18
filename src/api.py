from flask import (Blueprint, jsonify, request)
from . import blockchain

bp = Blueprint('api', __name__)

BlockchainInstance = blockchain.Blockchain()

@bp.route('/mine', methods=['POST'])
def mine():
    jsonData = request.get_json()
    print(jsonData)

    if all(k in jsonData for k in (BlockchainInstance.fields())):
        previous_block = BlockchainInstance.previousBlock()

        new_block = BlockchainInstance.createBlock(
            sender_name = jsonData['sender_name'],
            amount = jsonData['amount'],
            currency = jsonData['currency'],
            previous_hash = BlockchainInstance.hash(previous_block)
        )
        return jsonify(new_block), 200

    return jsonify({
        'error': 'Missing form data',
        'formData': jsonData
    }), 400

@bp.route('/chain', methods=['GET'])
def chain():
    return jsonify(BlockchainInstance.chain), 200
