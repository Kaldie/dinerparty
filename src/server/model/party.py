import datetime

from server.app import db
#pylint: disable=no-member
from sqlalchemy.orm import relationship
from sqlalchemy import exc
from .user import UserModel
from .party_participation import PartyParticipationModel


class PartyException(Exception):
    pass


class PartyModel(db.Model):
    __tablename__ = 'party'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True)
    latitude = db.Column(db.Float(5), default=0.0)
    longitude = db.Column(db.Float(5), default=0.0)
    description = db.Column(db.String, default="")
    seats = db.Column(db.Integer, default=1)
    teaching = db.Column(db.Boolean, default=False)
    cousin = db.Column(db.String(100), default="")
    date = db.Column(db.DateTime, default=datetime.datetime.now())
    image = db.Column(db.String(100), default='')

    # relations
    host_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    host = relationship("UserModel", back_populates='hosted_parties')

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
            PartyModel.query.filter_by(id=self.id, name=self.name).one()
        except:
            # TODO make better error handling
            raise

        db.session.commit()
        return self

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).one()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).one()

    @classmethod
    def find_by_host(cls, host_id):
        return cls.query.filder_by(host_id=host_id).all()

    @classmethod
    def find_by_range(cls, rangeDict):
        rangeDict["latitude"]["min"]

        return cls.query.filter(
            (cls.latitude >= rangeDict["latitude"]["min"]) &
            (cls.latitude <= rangeDict["latitude"]["max"]) &
            (cls.longitude >= rangeDict["longitude"]["min"]) &
            (cls.longitude <= rangeDict["longitude"]["max"])
        )

    @staticmethod
    def remove(party):
        try:
            db.session.delete(party)
            db.session.commit()
            return {"Message": "Party {} has been removed".format(party.name)}
        except Exception as error:
            raise error
            return {'message': 'something gone wrong!'}, 500
