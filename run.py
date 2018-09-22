from flask import Flask, jsonify, abort, request

app =  Flask(__name__)

orders = [
    {
        'orderId': 1,
        'orderTitle': 'Ghee',
        'orderDescription': 'Just what i want'
    },
    {
        'orderId': 2,
        'orderTitle': 'Corn',
        'orderDescription': 'I love corn too'
    },
    {
        'orderId': 3,
        'orderTitle': 'Milk',
        'orderDescription': 'I took lots of milk'
    }
]
#home page of the api


@app.route('/', methods=['GET'])
def index():
    return jsonify({'Welcome':"Hello"})

#displaying all the orders in the list


@app.route('/api/v1/orders', methods=['GET'])
def getOrders():
    return jsonify({'orders': orders})

#returning the data of a single order
@app.route('/api/v1/orders/<int:id>', methods=['GET'])
def getOrder(id):
    order = [order for order in orders if order['orderId'] == id]
    if len(order) == 0:
        abort(404)
    return jsonify({'order': order[0]})
#put

#implementing the post method


@app.route('/api/v1/orders', methods=['POST'])
def createOrder():
    if not request.json or not 'orderTitle' in request.json:
        abort(400)

    order = {
        'orderId': orders[-1]['orderId']+1,
        'orderTitle': request.json['orderTitle'],
        'orderDescription': request.json.get('orderDescription', "")
    }

    orders.append(order)
    return jsonify({'order': order}), 201


@app.route('/api/v1/orders/<int:id>', methods=['PUT'])
def updateOrder(id):
    order = [order for order in orders if order['orderId'] == id]
    if len(order) == 0:
        abort(404)

    if not request.json:
        abort(400)

    if 'orderTitle' in request.json and type(request.json['orderTitle']) != str:
        abort(400)

    if 'orderDescription' in request.json and type(request.json['orderDescription']) is not str:
        abort(400)

    order[0]['orderTitle'] = request.json.get(
        'orderTitle', order[0]['orderTitle'])
    order[0]['orderDescription'] = request.json.get(
        'orderDescription', order[0]['orderDescription'])
    return jsonify({'order': order[0]})
#delete
    
if __name__ == '__main__':
    app.run()
