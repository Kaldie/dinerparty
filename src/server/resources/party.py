from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from . import logger

from server.schema.party import PartySchema
from server.model.user import UserModel
from server.model.party import PartyModel, PartyException


class Party(Resource):
  @jwt_required
  def get(self, partyId):
    schema = PartySchema()
    return schema.load({"id": partyId}).data

  @jwt_required
  def post(self, partyId):
    party = PartySchema().load({"id": partyId}).data
    party.host_id = get_jwt_identity()["id"]
    
    try:
      party.addParty()
      return {"message": "Party created", "party":PartySchema().dump(party)}

    except PartyException as partyException:
      if "Party already exists" in str(partyException):
        return {"message": "Party already exists"}

    return {"message":"Unknown error!"}


  @jwt_required
  def patch(self, partyId):
    partySchema = PartySchema()
    party = partySchema.load({"id": partyId}).data
    logger.info("party: %s", partySchema.dump(party).data)
    party = partySchema.load(request.form, instance = party).data.update()
    return partySchema.dump(party)

  @jwt_required
  def delete(self, partyId):
    party = PartySchema(strict=True).load({"id": partyId}).data
    id = get_jwt_identity()["id"]
    if id == party.host_id:
      return PartyModel.remove(party)
    else:
      raise PartyException("You need to be the host to delete the party")


    