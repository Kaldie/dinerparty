from server.app import ma
from server.model.party import PartyModel

class PartySchema(ma.ModelSchema):
  class Meta:
    model = PartyModel
