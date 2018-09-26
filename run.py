from flask import Flask, jsonify, abort, request

app = Flask(__name__)

orders = []
# home page of the api


@app.route('/', methods=['GET'])
def index():
    return jsonify({'Welcome': "Hello"})

# displaying all the orders in the list


@app.route('/api/v1/orders', methods=['GET'])
def getOrders():
    if orders:
        return jsonify({'orders': orders})
    return jsonify({"Message": "No orders available"}), 200

# returning the data of a single order


@app.route('/api/v1/orders/<int:id>', methods=['GET'])
def getOrder(id):
    order = [order for order in orders if order['orderId'] == id]
    if len(order) == 0:
        abort(404)
    return jsonify({'order': order[0]})
# put

# implementing the post method


@app.route('/api/v1/orders', methods=['POST'])
def createOrder():
    if not request.json or not 'orderTitle' in request.json:
        abort(400)
    orderId = len(orders) + 1
    order = {
        'orderId': orderId,
        'orderTitle': request.json['orderTitle'],
        'orderDescription': request.json.get('orderDescription', ""),
        'orderStatus': 'pending'
    }

    orders.append(order)
    return jsonify({'order': order}), 201


@app.route('/api/v1/orders/<int:id>', methods=['PUT'])
def updateOrder(id):
    order = [order for order in orders if order['orderId'] == id]
    if len(order) == 0:
        abort(200)

    if not request.json:
        abort(400)

    if 'orderStatus' in request.json and type(request.json['orderStatus']) != str:
        abort(400)

    # if 'orderDescription' in request.json and type(request.json['orderDescription']) is not str:
    #     abort(400)

    order[0]['orderStatus'] = request.json.get(
        'orderStatus', order[0]['orderStatus'])
    # order[0]['orderDescription'] = request.json.get(
    #     'orderDescription', order[0]['orderDescription'])

    

    return jsonify({'order': order[0]})

# delete


@app.route('/api/v1/orders/<int:id>', methods=['DELETE'])
def deleteOrder(id):
    order = [order for order in orders if order['orderId'] == id]
    orders.remove(order[0])
    return jsonify({'orders': orders})


if __name__ == '__main__':
    app.run()
