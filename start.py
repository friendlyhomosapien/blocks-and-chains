import hashlib

from flask import Flask, jsonify

def hash(string):
    encodedString = str(string).encode()
    return hashlib.sha256(encodedString).hexdigest()

app = Flask(__name__)

@app.route("/")
def app():
    response = {
        'hash': 'test',
        'success': 'true',
        'previous_hash': hash('test')
    }
    return jsonify(response), 200
