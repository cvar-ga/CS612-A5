from flask import Flask, request
from flask_restful import Resource, Api
from json import loads
from flask import jsonify

# Initialize Flask
app = Flask(__name__)
api = Api(app)

@app.after_request
def add_cors_headers(response):
    try:
        r = request.referrer[:-1]
        response.headers.add('Access-Control-Allow-Origin', r)
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        response.headers.add('Access-Control-Allow-Headers', 'Accept')
        response.headers.add('Access-Control-Allow-Methods', 'GET')
        return response
    except Exception:
        return response

customers = []
with open('customers.json', 'r') as f:
    customers = loads(f.read())

class Customers(Resource):
    def get(self):
        return jsonify(customers)

class CustomerInfo(Resource):
    def get(self, cust_id):
        for item in customers:
            if item['cust_id'] == cust_id:
                return jsonify(item)
        return 404

class Orders(Resource):
    def get(self, cust_id):
        for item in customers:
            if item['cust_id'] == cust_id:
                return jsonify(item['orders'])
        return 404

class OrderInfo(Resource):
    def get(self, cust_id, order_id):
        for item in customers:
            if item['cust_id'] == cust_id:
                for order in item['orders']:
                    if order['order_id'] == order_id:
                        return jsonify(order)
        return 404

api.add_resource(Customers, '/customers')
api.add_resource(CustomerInfo, '/customers/<int:cust_id>')
api.add_resource(Orders, '/customers/<int:cust_id>/orders')
api.add_resource(OrderInfo, '/customers/<int:cust_id>/orders/<int:order_id>')

if __name__ == '__main__':
	app.run(host="0.0.0.0", debug=True)
