from server.app import ma
from marshmallow import Schema, fields, pprint
from server.model.party_participation import PartyParticipationModel
from server.schema.user import UserSchema, piiSensitive
from server.schema.party import PartySchema


class PartyParticipationSchema(ma.ModelSchema):
  
  user = fields.Nested(UserSchema, exclude=piiSensitive)
  party = fields.Nested(PartySchema, exclude=["host", "longitude", "latitude", "participation"])

  class Meta:
    model = PartyParticipationModel