from server.app import db
from sqlalchemy.orm import relationship
from sqlalchemy.orm.exc import NoResultFound
from .user import UserModel

from server.model import logger

from sqlalchemy import inspect


#pylint: disable=no-member

class PartyParticipationModel(db.Model):
    __tablename__ = "party_participation"

    id = db.Column(db.Integer, primary_key=True)
    hostAccepted = db.Column(db.Boolean, default=False, nullable=True)
    clientAccepted = db.Column(db.Boolean, default=False, nullable=True)

    # relations
    partyId = db.Column(db.Integer, db.ForeignKey('party.id'))
    userId = db.Column(db.Integer, db.ForeignKey('user.id'))

    # back ref
    user = relationship("UserModel", backref=db.backref("participation"))
    party = relationship("PartyModel", backref=db.backref("participation"))

    def addPartyParticipation(self):
        results = PartyParticipationModel.query.filter_by(party=self.party, user = self.user).all()
            
        assert len(results) <= 1  # for some reason, doing the query sets the state of self to persistent 
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        try:
            PartyParticipationModel.query.filter_by(id=self.id).one()
        except:
            # TODO make better error handling
            raise

        db.session.commit()
        return self

    @classmethod
    def delete_by_ids(cls, party, user):
        results = PartyParticipationModel.query.filter_by(party=party, user = user).all()
        for result in results:
            db.session.delete(result)

    @classmethod
    def find_by_ids(cls, party, user):
        logger.debug("party, user: %s, %s", party, user)
        return PartyParticipationModel.query.filter_by(party=party, user=user).all()

    @classmethod
    def find_participants_by_id(cls, partyId):
        return cls.query.filter_by(partyId=partyId).all()

    @classmethod
    def find_participants_by_name(cls, party_name):
        return cls.query.filter_by(party_name=party_name).all()

    @classmethod
    def count_participants_by_id(cls, partyId):
        return cls.find_participants_by_id(partyId).count()

    @classmethod
    def count_participants_by_name(cls, partyId):
        return cls.find_participants_by_name(partyId).count()

    @classmethod
    def count_coming(cls, partyId):
        return cls.accepting_users(partyId).count()

    @classmethod
    def count_decline(cls, partyId):
        return cls.declining_users(partyId).count()

    @classmethod
    def declining_users(cls, partyId):
        return cls.query.filter_by(partyId=partyId, clientAccepted=False).all()

    @classmethod
    def accepting_users(cls, partyId):
        return cls.query.filter_by(partyId=partyId, clientAccepted=True).all()

    @classmethod
    def count_replies(cls, partyId):
        return cls.query.filter_by(partyId=partyId).count()
