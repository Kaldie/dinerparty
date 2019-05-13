from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required
from server.model.parties import PartyModel
from server.model.party_participation import PartyParticipation
import json


class Party(Resource):
  
  parser = reqparse.RequestParser()
  parser.add_argument('name', help = 'Name of the party', required = True)
  parser.add_argument('description', help = 'Short description of the party', required = False)
  parser.add_argument('cousin', help = 'Type of cousin served at the party', required = False)
  parser.add_argument('image', help = 'This field cannot be blank', required = False)
  parser.add_argument('latitude', help = 'This field cannot be blank', required = False)
  parser.add_argument('longitude', help = 'This field cannot be blank', required = False)
  parser.add_argument('seats', type=int, help = 'This field cannot be blank', required = False)
  parser.add_argument('teaching', type=bool, help = 'This field cannot be blank', required = False)
  parser.add_argument('date', help = 'This field cannot be blank', required = False)


  def get(self):
    data = self.parser.parse_args()
    party = PartyModel.find_by_name(data['name'])
    return {"message": "Found party {}".format(party.name),
            "party":party.serialize}


  @jwt_required
  def post(self):
    data = self.parser.parse_args()
    party = PartyModel(**data)
    try:
      party.save_to_db()
      return {
        'message': 'Party {} has been created'.format(data['name'])
      }
    except Exception as exception:
      print(exception)
      return { 'message': "Something has gone wrong"}, 500


  def patch(self):
    data = self.parser.parse_args()  
    PartyModel.updateParty(data)

  
