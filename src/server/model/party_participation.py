from server.app import db
import datetime
from sqlalchemy.orm import relationship
from user import UserModel

class PartyParticipationModel(db.Model):
  __tablename__ = "party_participation"

  id = db.Column(db.Integer, primary_key = True)
  is_coming = db.Column(db.Boolean, default=True, nullable = True)
  is_accepted = db.Column(db.Boolean, default=True, nullable = True)
  
  # relations
  party_id = db.Column(db.Integer, db.ForeignKey('party.id') )
  user_id = db.Column(db.Integer, db.ForeignKey('user.id') )
  
  #back ref
  user = relationship("UserModel", backref = db.backref( "participation" ))
  party = relationship("PartyModel", backref = db.backref( "participation" ))


  @classmethod
  def find_participants_by_id(cls, party_id):
    return cls.query.filter_by(party_id = party_id)


  @classmethod
  def find_participants_by_name(cls, party_name):
    return cls.query.filter_by(party_name = party_name)


  @classmethod
  def count_participants_by_id(cls, party_id):
    return cls.find_participants_by_id().count()


  @classmethod
  def count_participants_by_name(cls, party_id):
    return cls.find_participants_by_name().count()


  def addParticipant(cls, party_id, user_id):
    entry = self.query.filter_by(party_id = party_id, user_id = user_id)
    
    if not entry:
      db.session.add(self)
    else:
      self.is_coming = True
      db.session.commit()


  def removeParticipant(self, party_id, user_id):
    entry = self.query.filter_by(party_id = party_id, user_id = user_id)
    
    if not entry:
      db.session.add(self)
    else:
      self.is_coming = False
      db.session.commit()


  @classmethod
  def count_coming(cls, party_id):
    return cls.accepting_users(party_id).count()


  @classmethod
  def count_decline(cls, party_id):
    return cls.declining_users(party_id).count()

  @classmethod
  def declining_users(cls, party_id):
    return cls.query.filter_by(party_id = party_id, is_coming = False)


  @classmethod
  def accepting_users(cls, party_id):
    return cls.query.filter_by(party_id = party_id, is_coming = True)


  @classmethod
  def count_replies(cls, party_id):
    return cls.query.filter_by(party_id = party_id).count()

