import unittest
from app import app


class BaseTestCase(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
