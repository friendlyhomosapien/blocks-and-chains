def test_chain(client):
    assert client.get('/chain').status_code == 200


def test_mine(client):
    assert client.post('/mine', json={
        'sender_name': 'Test user',
        'amount': 999,
        'currency': 'Bitcoin',
    }).status_code == 200


def test_mine_invalid_request(client):
    assert client.post('/mine', json={}).status_code != 200
