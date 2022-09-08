from flask import Flask, jsonify, request
from blockchain import Blockchain

app = Flask(__name__)

BlockChainInstance = Blockchain()

@app.route('/mine', methods=['POST'])
def mine():
    if 'user_name' in request.form and 'vote' in request.form:
        previous_block = BlockChainInstance.previousBlock()
        new_block = BlockChainInstance.createBlock(
            request.form['user_name'],
            request.form['vote'],
            BlockChainInstance.hash(previous_block)
        )
        return jsonify(new_block), 200

    return jsonify({
        'error': 'Missing form data'
    }), 400

@app.route('/chain', methods=['GET'])
def chain():
    return jsonify(BlockChainInstance.chain), 200
