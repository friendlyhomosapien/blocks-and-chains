import hashlib

from flask import Flask, jsonify

api = Flask(__name__)

@api.route("/", methods=['GET', 'POST'])
def app():
    response = {
        'hash': 'test',
        'success': 'true',
        'previous_hash': hashlib.sha256('test')
    }
    return jsonify(response), 200
