import datetime
from server.app import db, ma
from passlib.hash import pbkdf2_sha256
from sqlalchemy.orm import relationship


class UserModel(db.Model):
  __tablename__ = 'user'

  id = db.Column(db.Integer, primary_key = True)
  username = db.Column(db.String(120), unique = True, nullable = False)
  password = db.Column(db.String(120), nullable = False)
  email = db.Column(db.String(120))
  address = db.Column(db.String(120))
  postalCode = db.Column(db.String(120))
  city = db.Column(db.String(120))
  imagePath = db.Column(db.String(120))
  creationDate = db.Date()

  @staticmethod
  def generate_hash(password):
    print("password", password)
    if password.startswith("$pbkdf2-sha256") or password is "":
      print("return hash without hashing")
      return password
    print("hashing the bitch")
    return pbkdf2_sha256.hash(password)

  @staticmethod
  def verify_hash(password, hash):
    return pbkdf2_sha256.verify(password, hash)

  def addUser(self):
    self.creationDate = datetime.datetime.now()
    db.session.add(self)
    db.session.commit()
    return self

  def update(self):
    try:
      UserModel.query.filter_by(id = self.id, username=self.username).one()
    except:
      # TODO make beter error handling
      raise
    db.session.commit()
    return self

  @staticmethod
  def find_by_username(username):
    return UserModel.query.filter_by(username = username).one()

  @staticmethod
  def find_by_id(id):
    return UserModel.query.filter_by(id = id).one()

  @staticmethod
  def return_all():
    return UserModel.query.all()

  @staticmethod
  def delete_all():
    try:
      num_rows_deleted = UserModel.query.delete()
      db.session.commit()
      return {'message': '{} row(s) deleted'.format(num_rows_deleted)}
    except Exception as error:
      print(error)
      return {'message': 'something gone wrong!'}, 500

  @staticmethod
  def remove(user):
    try:
      db.session.delete(user)
      db.session.commit()
      return {"Message": "User {} has been removed".format(user.username)}
    except Exception as error:
      print(error)
      return {'message': 'something gone wrong!'}, 500
