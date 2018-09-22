import run
import unittest
import json


class TestRun(unittest.TestCase):
    """Class to test the methods in the run module"""
    
    def test_hello(self):
        #testing if the homepage can be reached
        self.client = run.app.test_client
        #self.app = run.app.test_client()

    def test_get_orders(self):
        """testing for all orders"""
        all_orders = self.client().get('api/v1/orders')
        self.assertEqual(all_orders.status_code, 200)

    def test_empty_order(self):
        """testing for when no order is placed"""
        empty_order = self.client().get('')
        self.assertEqual(empty_order.status_code, 404)

    def test_get_order(self):
        """fetching only one order test"""
        one_order = self.client().get('api/v1/orders/1')
        self.assertEqual(one_order.status_code, 200)

    def test_adding_order(self):
        """adding an order test"""
        added_order = self.client().post('api/v1/orders', content_type="application/json", data=json.loads(dict(orderId=1, orderTitle="Ghee" ,orderDescription="Just what i want")))
        call = json.dumps(added_order.data.decode("utf8"))
        self.assertIn('Ordered', call)
        self.assertIsInstance(call, dict)
        self.assertEqual(added_order.status_code, 200)
        self.assertTrue(added_order.json["Ordered"])
    



if __name__ == '__main__':
    unittest.main()
