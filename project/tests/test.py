import os
import unittest

from project import app


TEST_DB = 'test.db'


class BasicTests(unittest.TestCase):

    ############################
    #### setup and teardown ####
    ############################

    # executed prior to each test
    def setUp(self):

        self.app = app.test_client()
        self.app.testing = True 

    # executed after each test
    def tearDown(self):
        pass


###############
#### tests ####
###############

    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
