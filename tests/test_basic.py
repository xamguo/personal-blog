import unittest
from flask import current_app
from backend.app import create_app, db

class BasicTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('test').test_client()

    def tearDown(self):
        pass

    def test_app_exists(self):
        self.assertFalse(self.app is None)
        self.assertEqual(self.app.get('/').data, 'Hello world1!')
