from flask import Flask, render_template
from userApp import user_blueprint
from communityApp import community_blueprint

app = Flask(__name__)
app.register_blueprint(user_blueprint, url_prefix='/user')
app.register_blueprint(community_blueprint, url_prefix='/community')
app.secret_key = 'team20'


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)