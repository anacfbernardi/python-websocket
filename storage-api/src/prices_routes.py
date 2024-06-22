from __main__ import app

from flask import request

from .data import symbols
from .helpers import api_route

prices = []


@app.route(api_route('/prices'), methods=['GET'])
def prices_index():
    return prices


@app.route(api_route('/prices'), methods=['DELETE'])
def prices_clear():
    global prices
    prices = []
    return prices


@app.route(api_route('/prices/<id>'), methods=['GET'])
def prices_get(id):
    symbol_items = list(filter(lambda symbol: symbol['id'] == id, symbols))
    if len(symbol_items) > 0:
        price_items = list(filter(lambda price: price['symbol'] == id, prices))

        if len(price_items) > 0:
            return price_items[0]
        else:
            return {'message': 'price not found'}, 404

    else:
        return {'message': 'symbol not found'}, 404


@app.route(api_route('/prices/<id>'), methods=['POST'])
def prices_create(id):
    price = request.json['price']
    quantity = request.json['quantity']
    timestamp = request.json['timestamp']

    symbol_items = list(filter(lambda symbol: symbol['id'] == id, symbols))

    if len(symbol_items) > 0:
        price_items = list(filter(lambda price: price['symbol'] == id, prices))

        if len(price_items) > 0:
            price_item = price_items[0]

            price_item['price'] = price
            price_item['quantity'] = quantity
            price_item['timestamp'] = timestamp
        else:
            symbol_item = symbol_items[0]

            prices.append({
                'symbol': id,
                'symbolName': symbol_item['name'],
                'price': price,
                'quantity': quantity,
                'timestamp': timestamp
            })
    else:
        return {'message': 'symbol not found'}, 404

    return prices
