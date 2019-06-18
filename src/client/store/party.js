import { PartyService } from '@/client/service/party'
import { retryAfterTokenRefresh } from './utilities'
const state = {
  party: {}, 
  status: "undefined",
  foundParties: []
}

const actions = {
  registerParty({commit}, party) {
    retryAfterTokenRefresh(
      (party) => {
        commit("registerParty", party)
        return PartyService.registerParty(party)
      },
      party,
      result => commit("registerPartySucces", result),
      error => commit("registerPartyFailure", error)
    )
  },
  findParties({commit}, {currentLocation, range}) {
    retryAfterTokenRefresh(
      (currentLocation, range) => {
        commit("findingParties", currentLocation, range)
        return PartyService.findParties(currentLocation, range)
      },
      currentLocation, range,
      result => commit("findPartiesSucces", result),
      error => commit("findPartiesFailure", error)
    )
  }
}

const mutations = {
  registerParty(state, party) {
    state.status = "registeringParty"
    state.party = party
    state.foundParties = undefined
  },
  registerPartySucces(state, party) {
    state.status = "registeredParty"
    state.party = party
  },
  registerPartyFailure(state, error) {
    state.status = "failedToRegisterParty"
    state.error = error
  },
  findingParties(state, currentLocation, range) {
    state = {
      status : "findingParties",
      range,
      currentLocation 
    }
    state.party = {}
    state.foundParties = []
  },
  findPartiesSucces(state, result) {
    state.status = "foundParties" 
    state.foundParties = result.data
  },
  findPartiesFailure(state, error) {
    state.status = "failedToFindParties"
    state.error = error
    state.foundParties = []
  }
}

export const party = {
  namespaced: true,
  state,
  actions,
  mutations
}