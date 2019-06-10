
from flask import Flask, send_file

from flask_cors import CORS
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager

app = Flask(__name__, static_url_path="")

# add cross origin request sharing
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'some-secret-string'

app.config['JWT_SECRET_KEY'] = 'jwt-secret-string'
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']

api = Api(app)
db = SQLAlchemy(app)
ma = Marshmallow(app)
jwt = JWTManager(app)

# import model

from resources import users, party, parties, party_participation
#, 
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

api.add_resource(users.UserRegistration, '/registration')
api.add_resource(users.UserLogin, '/login')
api.add_resource(users.UserLogoutAccess, '/logout/access')
api.add_resource(users.UserLogoutRefresh, '/logout/refresh')
api.add_resource(users.TokenRefresh, '/token/refresh')
api.add_resource(users.PasswordModification, '/user/password')

api.add_resource(users.AllUsers, '/users')
api.add_resource(users.User,"/user")
api.add_resource(users.RequestUser,"/user/<string:id>")

api.add_resource(party.Party,'/party')
api.add_resource(parties.Parties,'/parties')
# api.add_resource(party_participation.PartyParticipation,'/party_participation')





