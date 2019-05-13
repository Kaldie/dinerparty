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
  seats = db.Column(db.Integer, default = 1)
  teaching = db.Column(db.Boolean, default = False)
  cousin = db.Column(db.String(100), default ="default cousin")
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
    """Return object data in easily serialize format"""
    return {
      'id' : self.id,
      'name': self.name,
      'latitude': self.latitude,
      'longitudinal': self.longitude,
      'description': self.description,
      'seats': self.seats,
      'teaching': self.teaching,
      'cousin': self.cousin,
      "date": dump_datetime(self.date),
      'image': self.image
    }
