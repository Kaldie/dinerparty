import { PartyService } from '@/client/service/party'
import { retryAfterTokenRefresh } from '@/client/utilities/RetryAfterTokenRefresh'
const state = {
  party: {}, 
  status: "undefined",
  foundParties: []
}

const actions = {

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