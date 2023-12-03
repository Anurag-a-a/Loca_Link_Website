import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app import app
import unittest

class EventTestCase(unittest.TestCase):

    def test_eventExplorer(self):
        tester = app.test_client(self)

        # Log in the user first
        response_login = tester.post(
            '/user/user_login',
            data=dict(username="Username", password="Password1234@"),
            follow_redirects=True
        )
        self.assertEqual(response_login.status_code, 200)

        response_event_explorer = tester.get('/community/eventExplorer', follow_redirects=True)
        self.assertEqual(response_event_explorer.status_code, 200)
        
        # Check if the eventExplorer.html template is used
        self.assertIn(b'Explore and participate', response_event_explorer.data)

    def test_userEvents(self):
        tester = app.test_client(self)

        # Log in the user first
        response_login = tester.post(
            '/user/user_login',
            data=dict(username="Username", password="Password1234@"),
            follow_redirects=True
        )
        self.assertEqual(response_login.status_code, 200)

        response_event_explorer = tester.get('/community/usersEvents', follow_redirects=True)
        self.assertEqual(response_event_explorer.status_code, 200)
        
        # Check if the eventExplorer.html template is used
        self.assertIn(b'List of the events that you created', response_event_explorer.data)

if __name__ == '__main__':
    unittest.main()
