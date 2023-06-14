from flask import Flask
from flask_cors import CORS
from api.v1.upload import upload

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:8080"}})

app.register_blueprint(upload)
