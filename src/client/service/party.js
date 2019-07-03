import { AuthHeader, CrossOriginHeader } from '@/client/utilities'
import objectToFormData from 'object-to-formdata'
import axios from 'axios'
import Settings from '@/client/settings.js'
import {retryAfterTokenRefresh} from '@/client/utilities'

axios.defaults.baseURL = `http://${Settings.server}:${Settings.port}/`


const registerParty = (party) => {
  retryAfterTokenRefresh(
    (party) => {
      const config = {
        headers: Object.assign(AuthHeader(), CrossOriginHeader),
      }
      const formData = objectToFormData(party)
      return axios.post(`party`, formData, config)
    },
    party
  )
}

const requestInvite = (partyId) => {
  retryAfterTokenRefresh(
    (partyId) => {
      let config = {
        headers: Object.assign(AuthHeader(), CrossOriginHeader),
      }
      axios.post(`/participations/${partyId}`, objectToFormData({}),config)
    },
    partyId
  )
}

const partyInforms = (party, decision, side) => {

  let partyKey = ""

  const formData = {partyId: party.id}

  if (side ==="client") {
    partyKey = "clientAccepted"
    
  } else if (side === "host") {
    partyKey = "hostAccepted"
  } else {
    throw Error("unkown side!")
  }

  formData[partyKey] = decision

  let config = {
    headers: Object.assign(AuthHeader(), CrossOriginHeader),
  }

  return axios.post('party_participation', objectToFormData(formData), config)
}

const updateParty = (party) => {
  retryAfterTokenRefresh(
    (party) => {
      let config = {
        headers: Object.assign(AuthHeader(), CrossOriginHeader),
      }
      return axios.patch(`party/${party.id}`, objectToFormData(party), config)
    },
    party
  )
}

const clientInforms = (party, decision) => {
  return partyInforms(party, decision, "client")
}

const hostsInforms = (party, decision) => {
  return partyInforms(party, decision, "client")
}

const clientAccepts = (party) => {
  clientInforms(party, true)
}

const clientRejects = (party) => {
  clientInforms(party, false)
}

const hostsAccepts = (party) => {
  hostsInforms(party,true)
}

const hostsRejects = (party) => {
  hostsInforms(party,false)
}

const getHostedParties = () => {
  const a = retryAfterTokenRefresh(
    () => {
      let config = {
        headers: Object.assign(AuthHeader(), CrossOriginHeader),
      }
      return axios.get(`me/parties`, config)
    },
  )
  return a
}

const findParties = (currentLocation, range) => {
  let config = {
    headers: Object.assign(AuthHeader(), CrossOriginHeader),
    params: {
      range,
      lat:currentLocation.lat,
      long: currentLocation.long,
    }
  }
  return axios.get('/parties/range', config)
}



export const PartyService = {
  registerParty,
  requestInvite,
  clientAccepts,
  clientRejects,
  hostsAccepts,
  hostsRejects,
  findParties,
  updateParty,
  getHostedParties
}