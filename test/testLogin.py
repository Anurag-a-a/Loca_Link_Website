import unittest
from app import app

class LoginTestCase(unittest.TestCase):

    def test_app_exists(self):
        self.assertFalse(app is None)

    def test_home_route(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)


    def test_user_login_page_loads(self):
        tester = app.test_client(self)
        response = tester.get('/user/user_login', content_type='html/text')
        self.assertTrue(b'Please input username and password' in response.data)


    def test_user_login(self):
        tester = app.test_client(self)
        response = tester.post(
            '/user/user_login',
            data=dict(username="UserName", password="Password123@"),
            follow_redirects=True
        )
        print("Status Code:", response.status_code)
        print("Headers:", response.headers)

        self.assertEqual(response.status_code, 200)

        redirect_url = response.headers.get('Location', '')
        print("Redirect URL:", redirect_url)
        self.assertTrue("/community/topPosts" in redirect_url)


    def test_user_logout(self):
        tester = app.test_client(self)
        tester.post(
            '/user/user_login',
            data=dict(username="UserName", password="Password123@"),
            follow_redirects=True
        )
        response = tester.get('/logout', follow_redirects=True)
        self.assertIn(b'You were logged out', response.data)


    def test_user_signup(self):
        tester = app.test_client(self)
        response = tester.post(
            '/user/signup',
            data=dict(username="newuser", password="newpass", confirm_password="newpass", email="newuser@example.com"),
            follow_redirects=True
        )
        self.assertIn(b'Account Created', response.data)


    def test_invalid_user_signup(self):
        tester = app.test_client(self)
        response = tester.post(
            '/user/signup',
            data=dict(username="", password="", confirm_password="", email=""),
            follow_redirects=True
        )
        self.assertIn(b'Please fill in all fields', response.data)

if __name__ == '__main__':
    unittest.main()
