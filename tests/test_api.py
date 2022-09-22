def test_add_transaction(client):
    assert client.post('/transactions', json={
        "sender": "Steven",
        "receiver": "receiver",
        "amount": 999,
        "currency": "USD"
    }).status_code == 200


def test_mine_invalid_request(client):
    assert client.post('/transactions', json={}).status_code != 200


def test_get_unconfirmed_transactions(client):
    assert client.get('/transactions').status_code == 200


def test_mine(client):
    test_add_transaction(client)
    assert client.post('/mine').status_code == 200


# def test_hash_rate(client):
#     assert client.get('/hash-rate').status_code == 200


def test_get_chain(client):
    assert client.get('/chain').status_code == 200


def test_validate_chain(client):
    assert client.post('/chain/validate').status_code == 200
