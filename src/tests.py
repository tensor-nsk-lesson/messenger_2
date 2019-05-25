import unittest
import requests


class TestUser(unittest.TestCase):

    def test_get_user(self):
        resp = requests.get('http://127.0.0.1/users')
        self.assertEqual(resp.status_code, 200)
        self.assertIsNotNone(resp.text)

    def test_add_user(self):
        data = {
            'name': 'HH',
            'age': 17
        }
        resp = requests.post('http://127.0.0.1/users', json=data)
        self.assertEqual(resp.status_code, 200)
        self.assertIsNotNone(resp.text)

