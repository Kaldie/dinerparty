from math import nan

from server.app import ma
from server.model.party import PartyModel
from server.schema.user import UserSchema
from marshmallow import fields

class PartySchema(ma.SQLAlchemyAutoSchema):
  host = fields.Nested(UserSchema, exclude=UserSchema.piiSensitive)

  class Meta:
    model = PartyModel
    load_instance = True
