from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from server.model.party_participation import PartyParticipationModel
from server.schema.party_participation import PartyParticipationSchema
import json


class PartyParticipationResource(Resource):

    @jwt_required
    def get(self):
        partyParticipation = \
            PartyParticipationSchema(partial=True).load(request.data).data

        coming = PartyParticipationModel.accepting_users(partyParticipation.id)
        declining = \
            PartyParticipationModel.declining_users(partyParticipation.id)

        return {
            'message': 'Party participation is {numberOfAccepting} accepted,\
                 {numberOfDeclining} declined'.format(
              numberOfDeclining=coming.count(),
              numberOfAccepting=declining.count()),
            "decliningParticipants": declining,
            "acceptingParticipants": coming
        }

    @jwt_required
    def post(self):
        partyParticipation = \
            PartyParticipationSchema(partial=True).load(request.data).data
        PartyParticipationModel.accepting_users(partyParticipation.id)

    @jwt_required
    def patch(self):
        if 'id' not in parser:
            raise ValueError("Need party id in request")
    
