from flask import Flask, render_template,send_from_directory
import os
from postApp import post_blueprint
from userApp import user_blueprint
from communityApp import community_blueprint
from eventApp import event_blueprint

app = Flask(__name__)
app.register_blueprint(user_blueprint, url_prefix='/user')
app.register_blueprint(community_blueprint, url_prefix='/community')
app.register_blueprint(post_blueprint, url_prefix='/post')
app.register_blueprint(event_blueprint, url_prefix='/event')
app.secret_key = 'team20'


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(os.path.join(app.root_path, 'uploads'), filename)


if __name__ == "__main__":
    app.run(debug=True)

