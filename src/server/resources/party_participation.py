import json
from server.resources import logger
from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from server.model.party_participation import PartyParticipationModel

from server.schema.party_participation import PartyParticipationSchema
from server.schema.party import PartySchema
from server.schema.user import UserSchema

class PartyParticipationResource(Resource):

    @jwt_required
    def get(self):
        partyParticipation = PartyParticipationSchema(partial=True).load(request.values).data

        coming = PartyParticipationModel.accepting_users(request.values.get("partyId"))
        declining = \
            PartyParticipationModel.declining_users(request.values.get("partyId"))
        logger.debug("coming: %s, declining %s", coming, declining)
        return {
            'message': 'Party participation is {numberOfAccepting} accepted, {numberOfDeclining} declined'.format(
              numberOfDeclining=len(declining),
              numberOfAccepting=len(coming)),
            "decliningParticipants": PartyParticipationSchema(many=True, partial=True).dump(declining),
            "acceptingParticipants": PartyParticipationSchema(many=True, partial=True).dump(coming)
        }

    @jwt_required
    def post(self):
        logger.debug("request.values: %s", request.values)
        party = PartySchema(strict=True).load({"id":request.values.get("partyId")}).data

        user = UserSchema(strict=True).load({
            "id": get_jwt_identity().get("id"),
            "username": get_jwt_identity().get("username")
            }).data

        participations = PartyParticipationModel.find_by_ids(party, user)
       
        if len(participations) == 0:
            participation = PartyParticipationSchema(partial=True).load(request.values).data
            participation.party = party
            participation.user = user
            participation.addPartyParticipation()

        elif len(participations) == 1:
            PartyParticipationSchema().load(request.values, instance = participations[0]).data.update()
        else:
            raise ValueError("returned more then 1 participation result. That's not possible")

        return {"message":"Added user {} as participant to party {}".format(user.username, party.name)}

    @jwt_required
    def patch(self):
        logger.debug("request.values: %s", request.values)
        party = PartySchema(strict=True).load({"id":request.values.get("partyId")}).data

        user = UserSchema(strict=True).load({
            "id": get_jwt_identity().get("id"),
            "username": get_jwt_identity().get("username")
            }).data
        
        participations = PartyParticipationModel.find_by_ids(party, user)
        if len(participations) != 1:
            raise ValueError("Could not find 1 or found more then 1 party participation!")

        participation = PartyParticipationSchema().load(request.values, instance = participations[0]).data
        participation.update()
        return {"message":"Updated participation",
                "participation": PartyParticipationSchema().dump(participation)}
