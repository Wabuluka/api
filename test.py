import unittest
from run import app

class TestRun(unittest.TestCase):
    """Class to test the methods in the run module"""

    def test_getOrders(self):
        #testing if the orders exist
        pass
    
    def test_getOrder(self):
        """Testing for Getting order per orderId"""
        pass

    def test_createOrder(self):
        """Testing for CreateOrder"""
        pass

    def test_updateOrder(self):
        """Testing for updateOrder"""
        pass

    def test_deleteOrder(self):
        """Testing for deleteOrder"""
        pass

if __name__ == '__main__':
    unittest.main()
