from . import logger
from server.app import ma
from marshmallow import Schema, fields, pprint


from server.model.party_participation import PartyParticipationModel
from server.schema.user import UserSchema
from server.schema.party import PartySchema

class PartyParticipationSchema(ma.SQLAlchemyAutoSchema):
 
  user = fields.Nested(UserSchema, exclude=UserSchema.piiSensitive)
  party = fields.Nested(PartySchema, exclude=["host", "longitude", "latitude", "participation"])

  class Meta:
    model = PartyParticipationModel
    load_instance = True

def sumerizeParticipation(participations):
  logger.debug("participations %s", participations)
  participationResult = {"pending": 0, "accepted": 0, "declined": 0  }
  for participation in participations:
    #if the host accepts, check the client
    logger.debug("participation %s", participation)
    if participation.hostResponse == PartyParticipationModel.ACCEPTED:
      if participation.clientResponse == PartyParticipationModel.ACCEPTED:
        participationResult["accepted"] += 1
      elif participation.clientResponse == PartyParticipationModel.UNKNOWN:
        participationResult["pending"] += 1
      elif participation.clientResponse == PartyParticipationModel.REJECTED:
        participationResult["declined"] += 1

    #If the hosts is pending, its pending
    if participation.hostResponse == PartyParticipationModel.UNKNOWN:
        participationResult["pending"] += 1
    
    #If the host rejects, its rejected
    if participation.hostResponse == PartyParticipationModel.REJECTED:
        participationResult["declined"] += 1
  
  return participationResult