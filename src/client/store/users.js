// import { userService } from '../services';
import { UserService } from '@/client/service/users'

const state = {
  all: {}
}

const actions = {
  getAll({ commit }) {
    commit ('getAllRequest')

    UserService.getAll().then(
      result => commit('getAllSuccess', result),
      error => commit('getAllFailure', error)
    )
  },

  delete({ commit }, id) {
    commit('deleteRequest', id)

    UserService.delete(id).then(
      result => commit('deleteSuccess', result),
      error => commit('deleteFailure', error)
    )
  },

  // get({commit}, id) {
  //   commit ("userGetRequest", id)

  //   UserService.getUser(id).then(
  //     result => commit('userGetSuccess', result),
  //     error => commit('userGetFailure', error)
  //   )
  // }
}

const mutations = {
  getAllRequest(state) {
    state.all = {loading: true}
  },
  getAllSuccess(state, users) {
    state.all = {items: users}
  },
  getAllFailure(state, error) {
    state.all = { error }
  },
  deleteRequest(state,id) {
    state.all.items = state.items.map(user => {
      if (user.id === id) {
        return {...user, deleting : true}
      }
      return user
    })
  },
  deleteSuccess(state, id) {
    state.all.items = state.all.items.filter(user => user.id !== id)
  },
  deleteFailure(state, {id, error} ) {
    state.all.items = state.all.items.map(user => {
      if (user.id === id) {
        // eslint-disable-next-line no-unused-vars
        const {deleting, ...userCopy} = user
        return {...userCopy, deleteError: error}
      }
    })
  }
}

export const users = {
  namespaced: true,
  state,
  actions,
  mutations
}

