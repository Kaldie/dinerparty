
from flask import Flask, send_file
from flask_restful import Api
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

from test_parties import testParties
from test_users import testUsers

import json

app = Flask(__name__, static_url_path="")

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'some-secret-string'

app.config['JWT_SECRET_KEY'] = 'jwt-secret-string'
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']

db = SQLAlchemy(app)
api = Api(app)
jwt = JWTManager(app)

# add cross origin request sharing
CORS(app)

import server.view.users
# from model.users import UsersModel
from resources import users, parties
from resources.party_participation import PartyParticipation
from model.revoked_token import RevokedTokenModel

Flask.env="debug"
Flask.Debug=True


@app.before_first_request
def create_tables():
  db.create_all()

@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    jti = decrypted_token['jti']
    return RevokedTokenModel.is_jti_blacklisted(jti)

@app.route("/")
def webpage():
  return send_file("/static/index.html")

# @app.route('/parties')
# def parties():
#   return json.dumps(testParties)


api.add_resource(users.UserRegistration, '/registration')
api.add_resource(users.UserLogin, '/login')
api.add_resource(users.UserLogoutAccess, '/logout/access')
api.add_resource(users.UserLogoutRefresh, '/logout/refresh')
api.add_resource(users.TokenRefresh, '/token/refresh')
api.add_resource(users.AllUsers, '/users')

api.add_resource(parties.Party,'/party')
api.add_resource(PartyParticipation,'/party_participation')





