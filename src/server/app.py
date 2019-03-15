
from flask import Flask, send_file
from flask_cors import CORS
from flask import request
from test_parties import testParties
import json

Flask.env="debug"
Flask.Debug=True

app = Flask(__name__, static_url_path="")

CORS(app)
@app.route("/")
def webpage():
  return send_file("/static/index.html")

@app.route('/parties')
def parties():
  print(request.args)
  return json.dumps(testParties)


