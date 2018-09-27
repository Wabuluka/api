from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

orders = []

# @app.route('/', methods=['GET'])
# def index(self):
#     self.message = 'You are welcome'
#     return jsonify{'Welcome': 'The app is working'}


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

if __name__ == '__main__':
    app.run(debug=True)
