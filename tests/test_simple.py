import unittest
import pocsidekicks


class ControllersTestCase(unittest.TestCase):
    def setUp(self):
        self.app = pocsidekicks.app.test_client()

    def tearDown(self):
        return

    def test_root(self):
        response = self.app.get('/')
        assert b'Hello World' in response.data
