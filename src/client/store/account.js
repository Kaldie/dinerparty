import { UserService } from '@/client/service/users'
import myRouter from '@/client/router'

const user = JSON.parse(localStorage.getItem('user'))

const state = user 
  ? {status: {loggedIn : true}, user} 
  : {status: {} , user: null}

const actions = {
  login({commit}, {userName, password}) {
    commit('loginRequest', { userName })

    UserService.login(userName, password)
      .then(
        result => {
          commit('loginSucces', result)
          myRouter.push('/')
        },
        error => commit('loginFailure', error)
      )
  },
  logout({ commit }) {
    UserService.logout()
    commit('logout')
  },
  register({ commit }, user) {
    commit('registerRequest', user)
    UserService.register(user)
      .then(
        result => {
          commit('registerSucces', result)
          myRouter.push('/')
        },
        error => commit('registerFailure', error)
      )
  },
  update({ commit }, user) {
    commit('updateRequest', user)
    UserService.update(user)
    .then(
      result => commit('updateSucces', result),
      error => commit('updateFailure', error)
    )
  },
  refresh( {commit} ) {
    commit('refresh')
    UserService.refresh()
    .then(
      result => {
        commit('refreshSucces', result)
      },
      error => {
        commit('refreshFailure', error)
      }
    )
  }
}

const mutations = {
  loginRequest(state, user) {
    state.status = {loggingIn: true}
    state.user = user
  },
  loginSucces(state, user) {
    state.status = {loggedIn: true}
    state.user = user
    localStorage.setItem('user', JSON.stringify(user))
  },
  loginFailure(state) {
    state.status = {loggedIn: false}
    state.user = null
    localStorage.removeItem('user')
  },
  logout(state) {
    state.status = {loggedIn: false}
    state.user = null
    localStorage.removeItem('user')
  },
  registerRequest(state) {
    state.status = {registering: true}
  },
  registerSucces(state, user) {
    state.status = {loggedIn: true}
    state.user = user
    localStorage.setItem('user', JSON.stringify(user))
  },
  registerFailure(state) {
    state.status = {}
    localStorage.removeItem('user')
  },
  updateRequest(state) {
    state.status = {loggingIn: true}
  },
  updateSuccess(state, user) {
    state.status = {loggedIn:true}
    state.user = user
  },
  updateFailure(state) {
    state.status = {}
    localStorage.removeItem('user')
  },
  refresh(state) {
    state.status = {logginIn: true}
  },
  refreshSucces(state, token) {
    state.status = {loggedIn: true}
    state.user.token = token
    localStorage.setItem('user', state.user)
  },
  refreshFailure(state) {
    state.status = {}
  }
}

export const account = {
  namespaced: true,
  state,
  actions,
  mutations
}

export const isLoggedIn = function() {
  if (state && state.status && state.status.loggedIn) {
    return state.status.loggedIn
  }
  return false
}