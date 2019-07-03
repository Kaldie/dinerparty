import random
import uuid
from . import logger
from sqlalchemy.orm.exc import NoResultFound
from flask import request
from flask_restful import Resource
from marshmallow import ValidationError
from flask_jwt_extended import create_access_token, create_refresh_token
from flask_jwt_extended import jwt_required, jwt_refresh_token_required, \
    get_jwt_identity, get_raw_jwt

from server.model.user import UserModel
from server.model.revoked_token import RevokedTokenModel
from server.schema.user import UserSchema


class UserException(Exception):
    pass


class UserRegistration(Resource):
    def post(self):
        try:
            newUser = UserSchema(partial=True).load(request.values).data
        except ValidationError:
            return "User is not properly defined:"

        try:
            UserModel.find_by_username(newUser.username)
            return {'message': 'User {} already exists'. format(
                newUser.username)}, 500

        except NoResultFound:
            pass

        try:
            newUser.addUser()
            access_token = create_access_token(
                identity={
                    "username": newUser.username,
                    "id": newUser.id
                })

            refresh_token = create_refresh_token(
                identity={
                    "username": newUser.username,
                    "id": newUser.id
                })

            return {
                'message': 'User {} has been created'.format(newUser.username),
                'access_token': access_token,
                'refresh_token': refresh_token,
                'user': UserSchema().dump(newUser)
            }

        except Exception as error:
            logger.error(error)
            return {'message': "Something has gone wrong"}, 500


class UserLogin(Resource):
    showDebugMessage = True
    message = staticmethod(lambda x: "Unknown user or password"
                           if not UserLogin.showDebugMessage else x)

    def post(self):
        logger.info("request.form: %s", request.form)
        user = UserSchema(partial=True).load(request.form).data
        logger.info(UserSchema().dump(user))
        if user.password is None:
            logger.warn("No password is provided during login")
            return {"message": UserLogin.message(
                "Username and password are required")}, 404

        try:
            databaseUser = UserModel.find_by_username(username=user.username)
        except NoResultFound:
            UserModel.verify_hash("randomness",
                                  UserModel.generate_hash(
                                    uuid.uuid4().hex[0:int(random.random()*20)]
                                    ))
            logger.warn("User did not exist: %s", user.username)
            return {'message':
                    UserLogin.message(
                        "Unknown User {}".format(user.username))
                    }, 404

        if UserModel.verify_hash(
                request.form["password"], databaseUser.password):

            access_token = create_access_token(
                identity={
                    "username": databaseUser.username,
                    "id": databaseUser.id
                })

            refresh_token = create_refresh_token(
                identity={
                    "username": databaseUser.username,
                    "id": databaseUser.id
                })

            return {'access_token': access_token,
                    'refresh_token': refresh_token,
                    'username': user.username,
                    'email': user.email
                    }
        else:
            logger.warn("Password did not exist for user: %s", user.username)
            return {
                "message": UserLogin.message(
                    "Unknown password {} for user {}".format(
                        request.form["password"], user.username))}, 404


class PasswordModification(Resource):
    showDebugMessage = True
    message = staticmethod(lambda x: "Unknown user or password"
                           if not UserLogin.showDebugMessage else x)

    @jwt_required
    def post(self):
        if "previousPassword" not in request.values \
                or request.values.get('previousPassword') is None:
            raise UserException("previousPassword is not set")

        if "newPassword" not in request.values or \
                request.values.get('newPassword') is None:
            raise UserException("previousPassword is not set")

        currentUserId = get_jwt_identity().get("id")
        databaseUser = UserModel.find_by_id(currentUserId)

        if not UserModel.verify_hash(
                request.values["previousPassword"], databaseUser.password):
            return {
                "message": PasswordModification.message(
                    "Previous password was not correct")}, 401

        databaseUser.password = \
            UserModel.generate_hash(request.values.get("newPassword"))
        databaseUser.update()
        return {"message": "Updated the password."}


class UserLogoutAccess(Resource):
    @jwt_required
    def post(self):
            jTokenId = get_raw_jwt()['jti']
            try:
                revoked_token = RevokedTokenModel(jTokenId=jTokenId)
                revoked_token.add()
                return {'message': 'Access token has been revoked'}
            except:
                    return {'message': 'Something went wrong'}, 500


class UserLogoutRefresh(Resource):
    @jwt_refresh_token_required
    def post(self):
            jTokenId = get_raw_jwt()['jti']
            try:
                revoked_token = RevokedTokenModel(jTokenId=jTokenId)
                revoked_token.add()
                return {'message': 'Refresh token has been revoked!'}
            except:
                    return {'message': 'Something went wrong'},
            return {"message": "Token has been revoked"}


class TokenRefresh(Resource):
        @jwt_refresh_token_required
        def post(self):
            current_user = get_jwt_identity()
            access_token = create_access_token(identity=current_user)
            return {'access_token': access_token}


class AllUsers(Resource):
    @jwt_required
    def get(self):
        return UserSchema().return_all()

    @jwt_required
    def delete(self):
        return UserModel.delete_all()


class User(Resource):

    @jwt_required
    def get(self):
        user = UserModel.find_by_id(get_jwt_identity()["id"])       
        return UserSchema().dump(user)

    @jwt_required
    def delete(self,):
        if userId == get_jwt_identity()["id"]:
            user = UserModel.find_by_id(get_jwt_identity()["id"])
            return UserModel.remove(user)
        else:
            return {"message": "Not allowed to delete an other user"}, 400

    @jwt_required
    def patch(self):
        userSchema = UserSchema()
        oldUser = UserModel.find_by_id(get_jwt_identity()["id"])
        logger.info("oldUser", oldUser.password)
        logger.info("request.form", request.form)
        updatedUser = userSchema.load(
            request.form, instance=oldUser).data.update()
        return userSchema.dump(updatedUser)


class RequestUser(Resource):
    @jwt_required
    def get(self, userName):
        logger.error("userName %s", userName)
        user = UserModel.find_by_username(userName)
        return UserSchema(exclude=UserSchema.piiSensitive).dump(user)