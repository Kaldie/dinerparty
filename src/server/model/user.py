from server.app import db
from passlib.hash import pbkdf2_sha256 as sha256

class UserModel(db.Model):
  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key = True)
  username = db.Column(db.String(120), unique = True, nullable = False)
  password = db.Column(db.String(120), nullable = False)
  email = db.Column(db.String(120))
  address = db.Column(db.String(120))
  postalCode = db.Column(db.String(120))
  city = db.Column(db.String(120))
  imagePath = db.Column(db.String(120))
  
  @staticmethod
  def generate_hash(password):
    return sha256.hash(password)

  @staticmethod
  def verify_hash(password, hash):
    print("hash", hash)
    return sha256.verify(password, hash)

  def save_to_db(self):
    db.session.add(self)
    db.session.commit()

  @classmethod
  def find_by_username(cls, username):
    return cls.query.filter_by(username= username).first()

  @classmethod
  def return_all(self):
    return {'users': list(map(lambda user: {
      'username'    : user.username,
      'password'    : user.password,
      'address'     : user.address,
      'postalCode'  : user.postalCode,
      'city'        : user.city,
      'imagePath'   : user.imagePath
    }, self.query.all()))}

  @classmethod
  def delete_all(cls):
    try:
      num_rows_deleted = db.session.query(cls).delete()
      db.session.commit()
      return {'message': '{} row(s) deleted'.format(num_rows_deleted)}
    except:
      return {'message': 'something gone wrong!'}, 500
