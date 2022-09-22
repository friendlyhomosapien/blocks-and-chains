> coverage run blockchain.py

> coverage report -m

> coverage html

# blockchain-demo

Demo blockchain app by Dave Ligthart.

## Install

`pipenv install`

## Run

`pipenv shell`

`FLASK_APP=src flask run`

`open http://127.0.0.1:5000/api/v1/blocks`

## Test

`pipenv shell`

`py.test`