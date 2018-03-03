import unittest
from flask import current_app
from backend.app import create_app, db

class BasicTestCase(unittest.TestCase):
    def setUp(self):
        print 'set up'
        self.app = create_app('test')

    def tearDown(self):
        print 'tear down'

    def test_app_exists(self):
        self.assertFalse(current_app is None)
