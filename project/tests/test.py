import os
import unittest
import requests
from project import app
from project.apis.opendota.Opendota import Opendota


class BasicTests(unittest.TestCase):

    ############################
    #### setup and teardown ####
    ############################

    # executed prior to each test
    def setUp(self):

        self.app = app.test_client()
        self.app.testing = True
        self.opendota_api = Opendota()

    # executed after each test
    def tearDown(self):
        pass


###############
#### tests ####
###############

    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_dota_page(self):
        response = self.app.get('/dota', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_dota_friends__page(self):
        response = self.app.get('/dota/friends', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_opendota_api_fail(self):
        self.opendota_api.BASE_URL = "http://google.com"
        self.assertIn("HTTPError", self.opendota_api.make_request('404.html'))

    def test_fortnite_page(self):
        response = self.app.get('/fortnite', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
