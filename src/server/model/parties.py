from server.app import db
from utilities import dump_datetime, load_datetime
import datetime

def replaceDateTimeString(dict):
    dict['date'] = load_datetime(dict.get('date',None))

class PartyModel(db.Model):
  __tablename__ = 'parties'

  id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String(120), unique = True, nullable = False)
  latitude = db.Column(db.Float(5), default = 0.0)
  longitude = db.Column(db.Float(5), default = 0.0)
  description = db.Column(db.String, default = "beautiful description")
  seets = db.Column(db.Integer, default = 1)
  teaching = db.Column(db.Boolean, default = False)
  cousine = db.Column(db.String(100), default ="default cousine")
  date = db.Column(db.DateTime, default = datetime.datetime.now())
  image = db.Column(db.String(100),default= 'None')

  def __repr__(self):
    return "Party({})".format(self.serialize)

  def save_to_db(self):
    if isinstance(self.date, basestring):
      self.date = load_datetime(self.date)
    db.session.add(self)
    db.session.commit()
  
  @classmethod
  def updateParty(cls, replace):
    replaceDateTimeString(replace)
    cls.query.filter_by(name = replace['name']).update(replace, synchronize_session = False)
    db.session.commit()

  @classmethod
  def find_by_name(cls, name):
    return cls.query.filter_by(name = name).first()

  @property
  def serialize(self):
    """Return object data in easily serializable format"""
    return {
      'id' : self.id,
      'name': self.name,
      'latitude': self.latitude,
      'longtitude': self.longitude,
      'description': self.description,
      'seets': self.seets,
      'teaching': self.teaching,
      'cousine': self.cousine,
      "date": dump_datetime(self.date),
      'image': self.image
    }

class PartyParticipation(db.Model):
  __tablename__ = "party_participation"

  id = db.Column(db.Integer, primary_key = True)
  party_id = db.Column(db.Integer, nullable = False)
  user_id = db.Column(db.Integer, nullable = False)
  is_coming = db.Column(db.Boolean, default=True, nullable = False)

  @classmethod
  def find_participants(cls, party_name):
    cls.query.filter_by(party_id = party_id)

  def add_participant(self, party_id, user_id):
    entry = self.query.filter_by(party_id = party_id, user_id = user_id)
    self.is_coming = True
    if not entry:
      db.session.add(self)
      db.session.commit()
    else:
      self.is_coming = True
      db.session.commit()

  def remove_participant(self, party_id, user_id):
    self.is_coming = False
    db.session.commit()

  @classmethod
  def count_coming(cls, party_id):
    return cls.query.filter_by(party_id = party_id, is_coming = True).count()

  @classmethod
  def count_decline(cls, party_id):
    return cls.query.filter_by(party_id = party_id, is_coming = False).count()

  @classmethod
  def count_replies(cls, party_id):
    return cls.query.filter_by(party_id = party_id).count()

