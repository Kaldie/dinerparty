from server.app import ma
from server.schema.user import UserSchema, piiSensitive
from server.model.party import PartyModel
from marshmallow import fields


class PartySchema(ma.ModelSchema):
  host = fields.Nested(UserSchema, exclude=piiSensitive)
  class Meta:
    model = PartyModel
    
