import { AuthHeader, CrossOriginHeader } from '@/client/utilities'
import objectToFormData from 'object-to-formdata'
import axios from 'axios'
import Settings from '@/client/settings.js'

axios.defaults.baseURL = `http://${Settings.server}:${Settings.port}/`

const registerParty = (party) => {
  let config = {
    headers: Object.assign(AuthHeader(), CrossOriginHeader),
  }
  return axios.post(`party`, objectToFormData(party), config)
}

const clientAccepts = (party) => {
  clientInforms(party, true)
}


const clientRejects = (party) => {
  clientInforms(party, false)
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

const clientInforms = (party, decision) => {
  return partyInforms(party, decision, "client")
}

const hostsInforms = (party, decision) => {
  return partyInforms(party, decision, "client")
}

const hostsAccepts = (party) => {
  hostsInforms(party,true)
}

const hostsRejects = (party) => {
  hostsInforms(party,false)
}

const getHostedParties = () => {
  return 1
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
  return axios.get('parties', config)
}

export const PartyService = {
  registerParty,
  clientAccepts,
  clientRejects,
  hostsAccepts,
  hostsRejects,
  findParties,
  getHostedParties
}