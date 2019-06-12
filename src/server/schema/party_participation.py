from server.app import ma
from marshmallow import Schema, fields, pprint
from server.model.party_participation import PartyParticipationModel

class PartyParticipationSchema(ma.ModelSchema):

  class Meta:
    model = PartyParticipationModel

  def return_all(self):
    print("UserModel.return_all()", self.dump(UserModel.return_all(), many=True))
    return self.dump(UserModel.return_all(), many=True)