import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app import app
import unittest


class PostsTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        self.tester = app.test_client(self)

    def test_Posts(self):
        tester = app.test_client(self)

        # Log in the user first
        response_login = tester.post(
            '/user/user_login',
            data=dict(username="Username", password="Password1234@"),
            follow_redirects=True
        )
        self.assertEqual(response_login.status_code, 200)

        response_event_explorer = tester.get('/community/topPosts', follow_redirects=True)
        self.assertEqual(response_event_explorer.status_code, 200)
        
        # Check if the eventExplorer.html template is used
        self.assertIn(b'div class="posts-container"', response_event_explorer.data)

    def test_user_posts(self):
        tester = app.test_client(self)

        # Log in the user first
        response_login = tester.post(
            '/user/user_login',
            data=dict(username="Username", password="Password1234@"),
            follow_redirects=True
        )
        self.assertEqual(response_login.status_code, 200)

        response_event_explorer = tester.get('/post/usersPosts', follow_redirects=True)
        self.assertEqual(response_event_explorer.status_code, 200)
        
        # Check if the eventExplorer.html template is used
        self.assertIn(b'<div class="content-container">', response_event_explorer.data)

    def test_create_post_success(self):
        # Log in the user first
        response_login = self.tester.post(
            '/user/user_login',
            data=dict(username="Username", password="Password1234@"),
            follow_redirects=True
        )
        self.assertEqual(response_login.status_code, 200)

        # Create a post
        response_create_post = self.tester.post(
            '/post/createPost',
            data=dict(title="New Title", content="Some content"),
            follow_redirects=True
        )

        self.assertEqual(response_create_post.status_code, 200)
        response_posts = self.tester.get('/community/1', follow_redirects=True)
        self.assertIn(b'Welcome to the Hoboken Community', response_posts.data)

    def test_create_post_title_used(self):
        # Log in the user first
        response_login = self.tester.post(
            '/user/user_login',
            data=dict(username="Username", password="Password1234@"),
            follow_redirects=True
        )
        self.assertEqual(response_login.status_code, 200)

        # Attempt to create a post with a title that has been used
        response_create_post = self.tester.post(
            '/post/createPost',
            data=dict(title="New Title", content="Some content"),
            follow_redirects=False
        )

        # Assuming the post creation fails due to the title being used, check for an error message or expected behavior
        self.assertEqual(response_create_post.status_code, 200)
        self.assertIn(b'alert("Title ', response_create_post.data)

    def test_create_post_title_with_curse_word(self):
        # Log in the user first
        response_login = self.tester.post(
            '/user/user_login',
            data=dict(username="Username", password="Password1234@"),
            follow_redirects=True
        )
        self.assertEqual(response_login.status_code, 200)

        # Attempt to create a post with a title that contains a curse word
        response_create_post = self.tester.post(
            '/post/createPost',
            data=dict(title="Title with fuck ", content="Some content"),
            follow_redirects=False
        )

        # Assuming the post creation fails due to the title containing a curse word, check for an error message or expected behavior
        self.assertEqual(response_create_post.status_code, 200)
        self.assertIn(b'alert("Title ', response_create_post.data)

    def test_deletePost_success(self):
        # Log in the user first
        response_login = self.tester.post(
            '/user/user_login',
            data=dict(username="Username", password="Password1234@"),
            follow_redirects=True
        )
        self.assertEqual(response_login.status_code, 200)
        # Get the post ID from the created post (you might need to adapt this part based on your application logic)
        
        response_delete_post = self.tester.post(
            f'/post/deletePost/2',
            follow_redirects=False
        )

        # Assuming the post deletion is successful, check for the success message
        self.assertEqual(response_delete_post.status_code, 200)
        self.assertIn(b'deleted successfully', response_delete_post.data)

    def test_delete_post_failure(self):
        # Log in the user first
        response_login = self.tester.post(
            '/user/user_login',
            data=dict(username="Username", password="Password1234@"),
            follow_redirects=True
        )
        self.assertEqual(response_login.status_code, 200)

        # Attempt to delete a non-existing post (you might need to adapt this part based on your application logic)
        response_delete_post = self.tester.post(
            '/post/deletePost/999',  # Assuming 999 is not a valid post ID
            follow_redirects=False
        )

        # Assuming the post deletion fails, check for the failure message
        self.assertEqual(response_delete_post.status_code, 200)
        self.assertIn(b'Failed to delete post', response_delete_post.data)

    def test_singlePosts(self):
        tester = app.test_client(self)

        from model.post import get_post_by_id
        # Attempt to delete the post

        post=    get_post_by_id(4)
        print(post)
        
        # Log in the user first
        response_login = tester.post(
            '/user/user_login',
            data=dict(username="Username", password="Password1234@"),
            follow_redirects=True
        )
        self.assertEqual(response_login.status_code, 200)

        response_event_explorer = tester.get('/post/3', follow_redirects=True)
        self.assertEqual(response_event_explorer.status_code, 200)
        
        # Check if the eventExplorer.html template is used
        self.assertIn(b'class="like-button"', response_event_explorer.data)


if __name__ == '__main__':
    unittest.main()
