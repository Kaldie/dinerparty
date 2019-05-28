from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from server.schema.party_schema import PartySchema
from server.model.user import UserModel
from server.model.party import PartyModel, PartyException


class Party(Resource):
  @jwt_required
  def get(self):
    party = PartySchema().load(request.form).data
    party= PartyModel.find_by_name(party.name)
    return {
      "message": "Found party {}".format(party.name),
      "party":PartySchema().dump(party)
    }

  @jwt_required
  def post(self):
    party = PartySchema(strict=True).load(request.form).data
    party.host_id = get_jwt_identity()["id"]
    try:
      party.addParty()
      return {"message": "Party created", "party":PartySchema().dump(party)}
    except PartyException as partyException:
      if "Party already exists" in str(partyException):
        return {"message": "Party already exists"}
      return {"message":"Unknown error!"}


  @jwt_required
  def patch(self):
    partySchema = PartySchema(strict=True)
    oldParty= PartyModel.find_by_name(request.form["name"])
    party = partySchema.load(request.form, instance = oldParty).data.update()
    return partySchema.dump(party)

  @jwt_required
  def delete(self):
    party = PartySchema().load(request.form).data
    print(party)
    if hasattr(party,"id") and party.id is not None:
      dbParty = PartyModel.find_by_id(party.id)
      return PartyModel.remove(dbParty)
    if hasattr(party,"name") and party.name is not None:
      dbParty = PartyModel.find_by_name(party.name)
      return PartyModel.remove(dbParty)
    raise PartyException("Could not find id or name")
      
    
