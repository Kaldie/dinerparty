import datetime

from server.app import db
from sqlalchemy.orm import relationship
from sqlalchemy import exc
from user import UserModel

class PartyException(Exception):
  pass

class PartyModel(db.Model):
  __tablename__ = 'party'

  id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String(120), unique = True, nullable = False)
  latitude = db.Column(db.Float(5), default = 0.0)
  longitude = db.Column(db.Float(5), default = 0.0)
  description = db.Column(db.String, default = "")
  seats = db.Column(db.Integer, default = 1)
  teaching = db.Column(db.Boolean, default = False)
  cousin = db.Column(db.String(100), default ="")
  date = db.Column(db.DateTime, default = datetime.datetime.now())
  image = db.Column(db.String(100),default= '')
  host_id =  db.Column(db.Integer, db.ForeignKey('user.id') )
  host = relationship( "UserModel", backref=db.backref('parties'))

  def addParty(self):
    try:
      db.session.add(self)
      db.session.commit()
    except exc.IntegrityError as exception:
      db.session.rollback()
      if "UNIQUE constraint failed: party.name" in str(exception):
        raise PartyException("Party already exists")
      else:
        raise exception

  def update(self):
    try:
      PartyModel.query.filter_by(id = self.id, name=self.name).one()
    except:
      # TODO make better error handling
      raise

    db.session.commit()
    return self

  @classmethod
  def find_by_name(cls, name):
    return cls.query.filter_by(name = name).one()

  @classmethod
  def find_by_id(cls, id):
    return cls.query.filter_by(id=id).one()

  @staticmethod
  def remove(party):
    try:
      print("here!!")
      db.session.delete(party)
      print("here2!!")
      db.session.commit()
      return {"Message": "Party {} has been removed".format(party.name)}
    except Exception as error:
      raise error
      return {'message': 'something gone wrong!'}, 500