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
  findParties
}