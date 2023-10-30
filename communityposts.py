from flask import Blueprint, jsonify
import pymysql

# Create a connection to the MySQL database
connection = pymysql.connect(
    host='localhost',
    user='your_username',
    password='your_password',
    database='team20'  # Replace 'team20' with your actual database name
)

posts_bp = Blueprint('posts', __name__)

# Endpoint to get posts by community
@posts_bp.route('/community/<int:community_id>/posts', methods=['GET'])
def get_posts_by_community(community_id):
    try:
        with connection.cursor() as cursor:
            # Execute the query to fetch posts for a specific community
            query = "SELECT * FROM post WHERE communityId = %s"
            cursor.execute(query, (community_id,))
            
            # Fetch all rows
            posts = cursor.fetchall()
            
            # Format the posts data if needed (e.g., converting to a list of dictionaries)
            formatted_posts = [{'id': post[0], 'userId': post[1], 'communityId': post[2], 'title': post[3], 'content': post[4], 'likeNum': post[5], 'isTop': post[6], 'createTime': post[7]} for post in posts]
            
            return jsonify(formatted_posts)

    except Exception as e:
        print("Error:", e)
        return jsonify({"error": "An error occurred while fetching posts"})

# Don't forget to close the database connection when the application terminates
@posts_bp.teardown_request
def close_connection(exception):
    connection.close()

posts = [
    {'id': 1, 'user_id': 1, 'content': 'Post 1 content'},
    {'id': 2, 'user_id': 2, 'content': 'Post 2 content'},
    # More posts...
]
@posts_bp.route('/delete_post/<int:post_id>', methods=['POST'])
def delete_post(post_id):
    # Get the post by its ID
    post = next((p for p in posts if p['id'] == post_id), None)
    if post:
        # Delete the post if the user_id matches (you may need to add authentication)
        if post['user_id'] == 1:  # Replace 1 with the user's ID who can delete posts
            posts.remove(post)
    
    return 'Post deleted successfully'  # You might redirect to another page after deletion
