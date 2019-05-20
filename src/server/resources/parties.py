from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from server.schema.party_schema import PartySchema
from server.model.user import UserModel
from server.model.party import PartyModel


class Party(Resource):

  def get(self):
    party = PartySchema(strict=True).load(request.form).data
    return {
      "message": "Found party {}".format(party.name),
      "party":PartySchema().dump(party)
    }

  @jwt_required
  def post(self):
    user = UserModel().find_by_username(get_jwt_identity()["username"])
    party = PartySchema(strict=True).load(request.form).data
    party.host_id = user.id
    try:
      party.addParty()
      return {
        'message': 'Party {} has been created'.format(party.name)
      }
    except Exception as exception:
      print(exception)
      return { 'message': "Something has gone wrong"}, 500


  def patch(self):
    partySchema = PartySchema(strict=True)
    oldParty= PartyModel.find_by_name(equest.form["name"])
    party = partySchema.load(request.form, instance = oldParty).data.update()
    return partySchema.dump(party)
