# from flask_restful import Resource, reqparse
# from flask_jwt_extended import jwt_required
# from server.model.party_participation import PartyParticipation
# import json

# class PartyParticipation(Resource):
#   parser = reqparse.RequestParser()
#   parser.add_argument("party_id", help = "Required parameter, identifying the party", required = True)
#   parser.add_argument("user_id", help = "Required parameter, identifying the user", required = True)
#   parser.add_argument("going", help = "Shows if you are participating or not", required = False, default = True)

#   @jwt_required
#   def get(self):
#     coming = PartyParticipation.accepting_users(parser.get('party_id'))
#     declining = PartyParticipation.declining_users(parser.get('party_i'))

#     return {
#       'message': 'Party participation is {numberOfAccepting} accepted, {numberOfDeclining} declined'.format(
#       numberOfDeclining= coming.count(),
#       numberOfAccepting= declining.count()),
#       "decliningParticipants": declining,
#       "acceptingParticipants": coming
#     }


#   @jwt_required
#   def patch(self):
#     if not 'id' in parser:
#       raise ValueError("Need party id in request")
  
