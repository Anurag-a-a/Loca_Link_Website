import unittest
from app import app

class LoginTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_login_success(self):
        response = self.app.post('/login', data={'username': '123456', 'password': '123456'})
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['username'], '123456')
        self.assertEqual(data['password'], '123456')


if __name__ == '__main__':
    unittest.main()
