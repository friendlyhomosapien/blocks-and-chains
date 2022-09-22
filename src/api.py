from flask import (Blueprint, jsonify, request)
from .Blockchain import Blockchain
from .Transaction import Transaction
from .HashRate import calcHashRate


bp = Blueprint('api', __name__)

BlockchainInstance = Blockchain()


@bp.route('/transactions', methods=['GET'])
def getTransactions():
    return BlockchainInstance.getUnconfirmedTransactions()


@bp.route('/transactions', methods=['POST'])
def addTransaction():
    jsonData = request.get_json()

    if all(k in jsonData for k in ([
        'sender', 'receiver', 'amount', 'currency'
    ])):

        BlockchainInstance.addTransaction(jsonData)

        return jsonify({
            'succes': True
        }), 200

    return jsonify({
        'error': 'Missing form data',
        'formData': jsonData
    }), 400


@bp.route('/hash-rate')
def hashRate():
    return calcHashRate(), 200


@bp.route('/mine', methods=['POST'])
def mine():
    if (BlockchainInstance.mineNext()):
        return jsonify({
            'success': True
        }), 200
    return jsonify({
        'success': False
    }), 500


@bp.route('/chain', methods=['GET'])
def getChain():
    BlockchainInstance.getChain()
    return jsonify({
        'chain': BlockchainInstance.getChain()
    }), 200


@bp.route('/chain/validate', methods=['POST'])
def chainValidate():
    if BlockchainInstance.validateChain():
        return jsonify({
            'success': True,
            'msg': 'chain is valid'
        }), 200

    return jsonify({
        'success': True,
        'msg': 'chain is invalid'
    }), 500
