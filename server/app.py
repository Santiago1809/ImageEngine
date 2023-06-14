from flask import Flask
from flask_cors import CORS
from api.v1.upload import upload

# This code is creating a Flask application instance named `app`. The `CORS` module is being used to
# enable Cross-Origin Resource Sharing (CORS) for the application, allowing requests from the
# specified origin (`http://localhost:8080`). The `upload` blueprint is being registered with the
# application, which contains routes and views for handling file uploads.
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:8080"}})

app.register_blueprint(upload)
