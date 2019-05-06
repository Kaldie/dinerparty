// import { userService } from '../services';
import { router } from '@/client/router';
import { userService } from '@/client/service/user'

const user = JSON.parse(localStorage.getItem('user'));

const state = user ? { status: { loggedIn: true }, user } : { status: {}, user: null };

const actions = {
  login({dispatched, commit}, {userName, password}) {
    commit('LoginRequest', {userName})

    userService.login(userName, password)
      .then( user => {
        state.user.status.loggidIn = true
        state.user = user 
      })
  }
}

