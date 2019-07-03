from . import logger

from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from sqlalchemy.orm.exc import NoResultFound

from server.model.party import PartyModel

from server.model.party_participation import PartyParticipationModel
from server.schema.party_participation import PartyParticipationSchema, sumerizeParticipation

from server.schema.party import PartySchema
from server.schema.user import UserSchema

def findParticipationWithFilter(partyId, identity, hostFilter, clientFilter ):
    party = PartySchema().load({"id": partyId}).data
    logger.debug("Party: %s", party)
    requesterId = identity.get("id")

    participations = []

    logger.debug("host: %s",party.host)
    logger.debug("requesterId: %s", requesterId)

    if party.host.id == requesterId:
        logger.debug("Host is getting participation")
        participations = PartyParticipationModel.find_participants_by_party_id(partyId)
        participations = filter(hostFilter , participations)
    else:
        logger.debug("Client is getting participation")
        participations = PartyParticipationModel.find_by_ids(partyId, requesterId)
        participations = filter(clientFilter , participations)
        
    return PartyParticipationSchema(many=True).dump(participations)


class PartyParticipations(Resource):

    @jwt_required
    def get(self, partyId):   
        partyParticipations = PartyParticipationModel.find_participants_by_party_id(partyId)
        logger.debug("partyParticipations %s",partyParticipations)

        sumery = sumerizeParticipation(partyParticipations)
       
        sumery.update({
            'message': 'Party participation: {} accepted, {} pending, {} rejected'.format(
                sumery.get("accepted", 0),
                sumery.get("pending", 0),
                sumery.get("rejected", 0))
                }, )
        return sumery
    
    @jwt_required
    def post(self, partyId):
        logger.debug("request.values: %s", request.values)
        try:
            party = PartyModel.find_by_id(partyId)
        except NoResultFound:
            return {"message": "Could not find party with id:{}".format(partyId)}, 404

        logger.debug("party: %s", party)

        user = UserSchema().load(get_jwt_identity()).data

        logger.debug("user: %s", user)

        if party.host.id == user.id:
            logger.error("Host cannot invite himself. UserName: %s, Party: %s", user.username, party.name)
            return {"message": "Host cannot invite himself"}, 400

        participations = PartyParticipationModel.find_by_ids(party.id, user.id)
       
        if len(participations) == 0:
            participation = PartyParticipationSchema(partial=True, transient=True).load(request.values).data
            participation.party = party
            participation.user = user
            participation.addPartyParticipation()
        else:
            logger.info("user: %s", user)
            logger.info("party: %s", party)
            logger.info("participations: %s", participations)
            logger.error("Fond participation, please use other routes to modify it.")
            return {"message": "Fond participation, please use other routes to modify it."}, 500

        return PartyParticipationSchema().dump(participation)

    @jwt_required
    def patch(self, partyId):
        logger.debug("request.values: %s", request.values)
        party = PartySchema().load({"id":partyId}).data

        user = UserSchema().load(get_jwt_identity()).data
        
        participations = PartyParticipationModel.find_by_ids(party, user)
        if len(participations) != 1:
            logger.info("user: %s", user)
            logger.info("party: %s", party)
            logger.info("participations: %s", participations)
            logger.warn("Could not find 1 or found more then 1 party participation")
            return {"message": "Could not find 1 or found more then 1 party participation!"}, 400

        participation = PartyParticipationSchema().load(request.values, instance = participations[0]).data
        participation.update()
        return PartyParticipationSchema().dump(participation)

class PendingPartyParticipations(Resource):

    @jwt_required
    def get(self, partyId):
        return findParticipationWithFilter(partyId, get_jwt_identity(), 
            lambda participation: participation.hostResponse == 0,
            lambda participation: participation.clientResponse == 0)


class PartyParticipation(Resource):

    @jwt_required
    def get(self, participationId):
        participation = PartyParticipationModel.find_by_id(participationId)
        logger.debug("PartyParticipation %s", participation)
        return PartySchema().dump(participation), 200

    @jwt_required
    def post(self, participationId):
        participation = PartyParticipationModel.find_by_id(participationId)
        identity = get_jwt_identity()

        if participation.party.host.id == identity.id:
            # Its the host
            participation.hostResponse = request.values.get("response")
        elif participation.user.id == identity.id:
            # Its the client
            participation.clientResponse = request.values.get("response")
        else:
            logger.info("identity: %s", identity)
            logger.info("participation: %s", participation)
            logger.warn("Identity did not match the participation host or client")
            return {"message": "Identity did not match the participation host or client!"}, 404
       
        return PartySchema().dump(participation), 200

    @jwt_required
    def patch(self, participationId):
        self.post(participationId)
