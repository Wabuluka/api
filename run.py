# from flask import Flask, jsonify, abort, request

# app = Flask(__name__)

# orders = []
# # home page of the api


# @app.route('/', methods=['GET'])
# def index():
#     return jsonify({'Welcome': "Hello"})

# # displaying all the orders in the list


# @app.route('/api/v1/orders', methods=['GET'])
# def getOrders():
#     if orders:
#         return jsonify({'orders': orders})
#     return jsonify({"Message": "No orders available"}), 200

# # returning the data of a single order


# @app.route('/api/v1/orders/<int:id>', methods=['GET'])
# def getOrder(id):
#     order = [order for order in orders if order['orderId'] == id]
#     if len(order) == 0:
#         abort(404)
#     return jsonify({'order': order[0]})
# # put

# # implementing the post method


# @app.route('/api/v1/orders', methods=['POST'])
# def createOrder():
#     if not request.json or not 'orderTitle' in request.json:
#         abort(400)
#     orderId = len(orders) + 1
#     order = {
#         'orderId': orderId,
#         'orderTitle': request.json['orderTitle'],
#         'orderDescription': request.json.get('orderDescription', ""),
#         'orderStatus': 'pending'
#     }

#     orders.append(order)
#     return jsonify({'order': order}), 201


# @app.route('/api/v1/orders/<int:id>', methods=['PUT'])
# def updateOrder(id):
#     order = [order for order in orders if order['orderId'] == id]
#     if len(order) == 0:
#         abort(200)

#     if not request.json:
#         abort(400)

#     if 'orderStatus' in request.json and type(request.json['orderStatus']) != str:
#         abort(400)

#     # if 'orderDescription' in request.json and type(request.json['orderDescription']) is not str:
#     #     abort(400)

#     order[0]['orderStatus'] = request.json.get(
#         'orderStatus', order[0]['orderStatus'])
#     # order[0]['orderDescription'] = request.json.get(
#     #     'orderDescription', order[0]['orderDescription'])

    

#     return jsonify({'order': order[0]})

# # delete


# @app.route('/api/v1/orders/<int:id>', methods=['DELETE'])
# def deleteOrder(id):
#     order = [order for order in orders if order['orderId'] == id]
#     orders.remove(order[0])
#     return jsonify({'orders': orders})


# if __name__ == '__main__':
#     app.run()
"""
    As advised by my LFA, I was required to change my API and use some elements of OOP otherthan 
    using hard code. Above is my previous API commented out and below is an improved version of the same 
    API this time using classes other than just function definitions.
"""

from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

orders = []


class AllOrders(Resource):
    """
    used to fetch all the orders available in the list
    """

    def get(self):
        return {'All orders available': orders}


class Order(Resource):
    """
        define functions to create, delete, get and update the order items
    """
    #getting one item

    def get(self, orderId):
        order = next(filter(lambda x: x['orderId'] == orderId, orders), None)
        return {'order': order}, 200 if order else 404

    #creating an order
    def post(self, orderId):
        if next(filter(lambda x: x['orderId'] == orderId, orders), None) is not None:
            return {'message': "An order with Order ID '{}' already exists." .format(orderId)}, 400

        data = request.get_json()
        order = {'orderId': orderId,
                 'orderTitle': data['orderTitle'],
                 'orderDescription': data['orderDescription']}
        orders.append(order)
        return order, 201

    #deleting an order
    def delete(self, orderId):
        global orders
        orders = list(filter(lambda x: x['orderId'] != orderId, orders))
        return {'message': 'Order has been successfuly deleted'}

    #updating an order
    def put(self, orderId):
        data = request.get_json()
        order = next(filter(lambda x: x['orderId'] == orderId, orders), None)
        if order is None:
            order = {'orderId': orderId,
                     'orderTitle': data['orderTitle'],
                     'orderDescription': data['orderDescription']}
            orders.append(order)
        else:
            order.update(data)


#url that connects to the AllOrders class
api.add_resource(AllOrders, '/api/v1/orders')
#url that connects to the order class
api.add_resource(Order, '/api/v1/order/<int:orderId>')


app.run(debug=True)
