import run
import unittest
import json


class TestRun(unittest.TestCase):
    """Class to test the methods in the run module"""
    #client = run.app.test_client

    def setUp(self):
       self.app = run.app.test_client()

    # def test_hello(self):
    #     #testing if the homepage can be reached
    #     #self.client = run.app.test_client
    #     #self.app = run.app.test_client()
    #     pass

    # def test_get_orders(self):
    #     """testing for all orders"""
    #     all_orders = self.app.get('api/v1/orders')
    #     self.assertEqual(all_orders.status_code, 200)

    # def test_empty_order(self):
    #     """testing for when no order is placed"""
    #     empty_order = self.app.get('')
    #     self.assertEqual(empty_order.status_code, 301)

    # def test_get_order(self):
    #     """fetching only one order test"""
    #     one_order = self.app.get('api/v1/orders/1')
    #     self.assertEqual(one_order.status_code, 404)

    def test_adding_order(self):
        """adding an order test"""
        post_data = {
            'orderId': 1,
            'orderTitle': 'Ghee',
            'orderDescription': 'Just what i want',
            'orderStatus': 'pending'
        }
        added_order = self.app.post('api/v1/orders', content_type="application/json", data=json.dumps(post_data))
        #call = json.dumps(added_order.data.decode("utf8"))
        # self.assertIn('Ordered', call)
        # self.assertIsInstance(call, dict)
        self.assertEqual(added_order.status_code, 201)
        # self.assertTrue(added_order.json["Ordered"])
    



if __name__ == '__main__':
    unittest.main()
