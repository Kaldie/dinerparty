
import { UserService } from '@/client/service/users'
import myRouter from '@/client/router'
import { retryAfterTokenRefresh } from './utilities'

let user
try {
  user = JSON.parse(localStorage.getItem('user'))
} catch {
  localStorage.removeItem("user")
}

const state = user 
  ? {status: {loggedIn : true}, user} 
  : {status: {} , user: {}}


const actions = {
  login({commit}, {username, password}) {
    commit('loginRequest', { username })
    return UserService.login(username, password)
      .then(
        result => {
          commit('loginSucces', result.data)
          myRouter.push('/')
        },
        error => {commit('loginFailure', error)}
      )
  },
  logout({ commit }) {
    UserService.logout()
    commit('logout')
  },
  register({ commit }, user) {
    commit('registerRequest', user)
    return UserService.register(user)
      .then(
        result => {
          commit('registerSucces', result.data)
          myRouter.push('/')
        },
        error => commit('registerFailure', error)
      )
  },
  get({commit}) {
    retryAfterTokenRefresh(
      () => {commit('getUserRequest'); return UserService.get() },
      (result) => commit('getUserSucces', result),
      (error) => commit('getUserFailure', error)
    )
  },
  update({ commit }, user) {
    retryAfterTokenRefresh(
      (user) => {
        commit('updateRequest', user)
        return UserService.update(user) 
      },
      user,
      result => commit('updateSucces', result),
      error => commit('updateFailure', error)
    )
  },
  refresh({ commit }) {
    commit('refresh')
    return UserService.refreshToken()
    .then(
      result => commit('refreshSucces', result),
      error => commit('refreshFailure', error)
    )
  },
  resetPassword({commit}, passwordObject) {
    retryAfterTokenRefresh(
      (passwordObject) => {
          commit('resetPassword')
          return UserService.resetPassword(passwordObject)
      },
      passwordObject,
      () => commit("resetPasswordSucces"),
      error => commit("resetPasswordFailure", error)
    )
  },
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
    state.user = {}
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
  updateSucces(state, user) {
    state.status = {loggedIn:true}
    state.user = Object.assign(state.user, user.data)
  },
  updateFailure(state) {
    state.status = {}
    localStorage.removeItem('user')
  },
  getUserRequest(state) {
    state.status = {
      loggedIn:true, 
      requestingInfo:true
    }
  },
  getUserSucces(state, result) {
     state.user = Object.assign(state.user, result.data)
     state.status = {
       loggedIn: true,
       requestInfoSucces : true
     }
  },
  getUserFailure(state, error){
    state.status = {
      requestInfoSucces : false,
      loggedIn: false,
      error
    }
    state.user = Object.assign(state.user, {username:""})
  },
  refresh(state) {
    state.status = {logginIn: true}
  },
  refreshSucces(state, access_token) {
    state.status = {loggedIn: true}
    state.user.access_token = access_token
    localStorage.setItem('user', state.user)
  },
  resetPassword(state) {
    state.status = {loggedIn:true, resetingPassword: true}
  },
  resetPasswordSucces(state) {
    state.status = {loggedIn:true, resetPassword: true}
  },
  resetPasswordFailure(state) {
    state.status = {loggedIn:true, resetPassword: false}
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