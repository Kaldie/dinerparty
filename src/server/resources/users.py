import random
import uuid
from sqlalchemy.orm.exc import NoResultFound
from flask import request
from flask_restful import Resource
from marshmallow import ValidationError
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt

from server.model.user import UserModel
from server.model.revoked_token import RevokedTokenModel
from server.schema.user_schema import UserSchema

class UserRegistration(Resource):
  def post(self):
    try:
      newUser = UserSchema(strict=True).load(request.form).data
    except ValidationError as validationError:
      return "User is not properly defined:"

    try:
      UserModel.find_by_username(newUser.username)
      return {'message': 'User {} already exists'. format(newUser.username)}, 500
    except NoResultFound:
      pass

    try:
      newUser.addUser()
      access_token = create_access_token(identity = {"username": newUser.username, "id": newUser.id})
      refresh_token = create_refresh_token(identity = {"username": newUser.username, "id": newUser.id})
      return {
        'message': 'User {} has been created'.format(newUser.username),
        'access_token': access_token,
        'refresh_token': refresh_token,
        'user': UserSchema().dump(newUser)
      }
    except Exception as error:
      print(error)
      return { 'message': "Something has gone wrong"}, 500

class UserLogin(Resource):
  showDebugMessage = True
  message = staticmethod(lambda x: "Unknown user or password" if not UserLogin.showDebugMessage else x)

  def post(self):
    user = UserSchema().load(request.form).data

    if (not isinstance(user, UserModel)) or user.password is None:
      return {"message": UserLogin.message("Username and password are required")}, 404

    databaseUser = UserModel.find_by_username(username=user.username)
    if not databaseUser:
      UserModel.verify_hash("randomasss", UserModel.generate_hash(uuid.uuid4().hex[0:int(random.random()*20)]))
      return {'message': UserLogin.message("Unknown User {}".format(user.username))}, 404

    if UserModel.verify_hash(request.form["password"], databaseUser.password):
      access_token = create_access_token(identity = {"username": databaseUser.username, "id": databaseUser.id})
      refresh_token = create_refresh_token(identity = {"username": databaseUser.username, "id": databaseUser.id})
      return {'message': 'Logged in as {}'.format(user.username),
              'access_token': access_token,
              'refresh_token': refresh_token,
              'username': user.username,
              'email': user.email}
    else:
      return {"message": UserLogin.message("Unknown password {} for user {}".format(request.form["password"], user.username))}, 404

class UserLogoutAccess(Resource):
  @jwt_required
  def post(self):
      jTokenId = get_raw_jwt()['jti']
      try:
        revoked_token = RevokedTokenModel(jTokenId = jTokenId)
        revoked_token.add()
        return {'message': 'Access token has been revoked'}
      except:
          return {'message': 'Something went wrong'}, 500
      
class UserLogoutRefresh(Resource):
  @jwt_refresh_token_required
  def post(self):
      jTokenId = get_raw_jwt()['jti']
      try:
        revoked_token = RevokedTokenModel(jTokenId = jTokenId)
        revoked_token.add()
        return {'message': 'Refresh token has been revoked!'}
      except:
          return {'message': 'Something went wrong'}, 
      return {"message":"Token has been revoked"}
      
class TokenRefresh(Resource):
    @jwt_refresh_token_required
    def post(self):
      current_user = get_jwt_identity()
      access_token = create_access_token(identity = current_user)
      return {'access_token': access_token}
    
class AllUsers(Resource):
  @jwt_required
  def get(self):
    return UserSchema().return_all()

  def delete(self):
    return UserModel.delete_all()

class User(Resource):
  @jwt_required
  def get(self):
    user = UserModel.find_by_id(get_jwt_identity()["id"])
    return UserSchema().dump(user)

  @jwt_required
  def patch(self):
    userSchema = UserSchema()
    oldUser = UserModel.find_by_id(get_jwt_identity()["id"])
    updatedUser = userSchema.load(request.form, instance = oldUser).data.update()
    return userSchema.dump(updatedUser)
    