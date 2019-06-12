from server.app import ma
from marshmallow import Schema, fields, pprint
from server.model.user import UserModel

class UserSchema(ma.ModelSchema):
  email = fields.Email()
  password = fields.Function(deserialize = lambda password: UserModel.generate_hash(password), load_only=True,)
  
  class Meta:
    model = UserModel

  def return_all(self):
    print("UserModel.return_all()", self.dump(UserModel.return_all(), many=True))
    return self.dump(UserModel.return_all(), many=True)