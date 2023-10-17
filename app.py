from flask import Flask, render_template
from flask import redirect
from flask import url_for
from flask import request
from model.login import is_existed, exist_user, is_null
from model.signup import add_user

app = Flask(__name__)


@app.route('/')
def index():
    return redirect(url_for('user_login'))


@app.route('/user_login', methods=['GET', 'POST'])
def user_login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if is_null(username, password):
            login_massage = "Please input correctly. "
            return render_template('login.html', message=login_massage)
        elif is_existed(username, password):
            return render_template('index.html', username=username)
        elif exist_user(username):
            login_massage = "Please input correctly. "
            return render_template('login.html', message=login_massage)
        else:
            login_massage = "Please input correctly. "
            return render_template('login.html', message=login_massage)
    return render_template('login.html')


@app.route("/signup", methods=["GET", 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if is_null(username, password):
            login_massage = "Please input correctly. "
            return render_template('signup.html', message=login_massage)
        elif exist_user(username):
            login_massage = "Please input correctly. "
            # return redirect(url_for('user_login'))
            return render_template('signup.html', message=login_massage)
        else:
            add_user(request.form['username'], request.form['password'])
            return render_template('index.html', username=username)
    return render_template('signup.html')


if __name__ == "__main__":
    app.run()