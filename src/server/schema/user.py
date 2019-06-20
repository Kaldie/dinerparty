from server.app import ma
from marshmallow import Schema, fields, pprint
from server.model.user import UserModel
from server.model.party import PartyModel
from server.model.party_participation import PartyParticipationModel


class UserSchema(ma.ModelSchema):
  piiSensitive = ["hosted_parties", "postalCode", "address", "city",'email']
  email = fields.Email()
  password = fields.Function(deserialize = lambda password: UserModel.generate_hash(password), load_only=True,)
  
  class Meta:
    model = UserModel

  def return_all(self):
    print("UserModel.return_all()", self.dump(UserModel.return_all(), many=True))
    return self.dump(UserModel.return_all(), many=True)