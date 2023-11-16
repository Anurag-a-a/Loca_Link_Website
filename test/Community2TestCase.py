import unittest
import json

from app import app

class Community2TestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_community(self):
        response = self.app.get('/community2/1')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['name'], 'Arts')
        self.assertEqual(data['description'], "Here you can find posts related to arts")

        response = self.app.get('/community2/5')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
