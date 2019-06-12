import logging
from flask import request
from math import radians, sin, cos, acos

from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from server.schema.party import PartySchema
from server.model.user import UserModel
from server.model.party import PartyModel, PartyException


# gotten from
# https://www.w3resource.com/python-exercises/math/python-math-exercise-27.php
def distanceBetween(partyLocation, currentLocation):
    assert(partyLocation and currentLocation)

    assert((partyLocation.get("long", None) is not None) and
           (partyLocation.get("lat", None) is not None))

    assert((currentLocation.get("long", None) is not None) and
           (currentLocation.get("lat", None) is not None))

    r1 = radians(partyLocation.get("lat"))
    r2 = radians(currentLocation.get("lat"))
    dl = radians(currentLocation.get("long") - partyLocation.get("long"))
    R = 637.1  # gives d in km
    return acos(sin(r1) * sin(r2) + cos(r1) * cos(r2) * cos(dl)) * R


def approximateValidRange(location, distance):
    rangeApproximation = {
        "latitude": {"max": None, "min": None},
        "longitude": {"max": None, "min": None}
    }

    # https://www.thoughtco.com/degree-of-latitude-and-longitude-distance-4070616
    distanceOfOneDegreeOfLatitude = 111
    rangeApproximation["latitude"]["min"] = \
        location["lat"] - (distance / distanceOfOneDegreeOfLatitude)
    rangeApproximation["latitude"]["max"] = \
        location["lat"] + (distance / distanceOfOneDegreeOfLatitude)

    # Determine the latitude which given 1
    # degree difference is the least distance
    lat = radians(min(abs(rangeApproximation["latitude"]["min"]),
                      abs(rangeApproximation["latitude"]["max"])))
    a = 1
    distanceOfOneDegreeOfLong = distanceOfOneDegreeOfLatitude * cos(lat)
    rangeApproximation["longitude"]["min"] = \
        location["long"] - (distance / distanceOfOneDegreeOfLong)
    rangeApproximation["longitude"]["max"] = \
        location["long"] + (distance / distanceOfOneDegreeOfLong)
    return rangeApproximation


class Parties(Resource):
    @jwt_required
    def get(self):
        values = request.values
        assert(values.get("lat", None))
        assert(values.get("long", None))

        partyRange = float(values.get("range", 10))
        logging.info("partyRange", partyRange)

        currentPosition = {
            "lat": float(values.get("lat")),
            "long": float(values.get('long'))
        }

        validRange = approximateValidRange(currentPosition, partyRange)
        parties = PartyModel.find_by_range(validRange)

        validParties = []
        for party in parties:
            partyLocation = {"long": party.longitude, "lat": party.longitude}

            if distanceBetween(partyLocation, currentPosition) <= partyRange:
                validParties.append(party)

        return PartySchema().dump(validParties, many=True)