from flask import Flask, session
from flask import redirect
from flask import url_for
from userApp import user_blueprint

app = Flask(__name__)
app.register_blueprint(user_blueprint, url_prefix='/user')
app.secret_key = 'team20'


@app.route('/')
def index():
    return redirect(url_for('user.user_login'))


if __name__ == "__main__":
    app.run()