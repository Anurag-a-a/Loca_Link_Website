import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app import app
import unittest

class LoginTestCase(unittest.TestCase):

    def test_user_login(self):
        tester = app.test_client(self)
        response = tester.post(
            '/user/user_login',
            data=dict(username="Username", password="Password1234@"),
            follow_redirects=True
        )
        self.assertEqual(response.status_code, 200)

    def test_user_logout(self):
        tester = app.test_client(self)

        # Log in the user first
        response_login = tester.post(
            '/user/user_login',
            data=dict(username="Username", password="Password1234@"),
            follow_redirects=True
        )
        self.assertEqual(response_login.status_code, 200)

        # Check that the user is logged in
        response_before_logout = tester.get('/community/topPosts', content_type='html/text')
        print(response_before_logout)
        self.assertTrue(b'Welcome to your Virtual Community' in response_before_logout.data)

        # Logout the user
        response_logout = tester.get('/user/logout', follow_redirects=True)
        self.assertEqual(response_logout.status_code, 200)

        # Check that the user is now logged out
        response_after_logout = tester.get('user/user_login', content_type='html/text')
        print(response_after_logout)
        self.assertTrue(b'Welcome, Username!' not in response_after_logout.data)
        self.assertTrue(b"Login" in response_after_logout.data)

    def test_profile(self):
        tester = app.test_client(self)

        # Log in the user first
        response_login = tester.post(
            '/user/user_login',
            data=dict(username="Username", password="Password1234@"),
            follow_redirects=True
        )
        self.assertEqual(response_login.status_code, 200)

        # Check that the user is logged in
        response_before_logout = tester.get('/user/profile', content_type='html/text')
        self.assertTrue(b'User Profile' in response_before_logout.data)
        self.assertTrue(b'Username' in response_before_logout.data)
        




if __name__ == '__main__':
    unittest.main()
