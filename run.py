from flask import Flask, jsonify, abort

app = Flask(__name__)
orders = [
    {
        'orderId': 1,
        'orderTitle': u'Ghee',
        'orderDescription': u'Just what i want'
    },
    {
        'orderId': 2,
        'orderTitle': u'Corn',
        'orderDescription': u'I love corn too'
    },
    {
        'orderId': 3,
        'orderTitle': u'Milk',
        'orderDescription': u'I took lots of milk'
    }
]
#home page of the api


@app.route('/')
def index():
    return "Hello"

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

if __name__ == '__main__':
    app.run(debug=True)
