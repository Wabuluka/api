import unittest
from run import app

class HomePageTest(unittest.TestCase):

    def test_getOrders(self):
        response = run.test_client()
        self.assertEquals(response.status_code, 200)



if __name__ == '__main__':
    unittest.main()
