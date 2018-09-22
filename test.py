import run
import unittest
import json


class TestRun(unittest.TestCase):
    """Class to test the methods in the run module"""
    
    def test_hello(self):
        #testing if the homepage can be reached
        pass

    def test_getOrders(self):
        #testing if the orders exist
        self.assertFalse(run.getOrders())
        self.assertEqual(len(run.getOrders()), 0)
        #rep = client.post('/api/v1/orders', data=json.dumps('orders'))


if __name__ == '__main__':
    unittest.main()
