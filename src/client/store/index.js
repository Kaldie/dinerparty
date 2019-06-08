import Vue from 'vue';
import Vuex from 'vuex';

// import { alert } from './alert.module';
import { users } from './users';
import { account, isLoggedIn } from './account';
import { party } from './party'

export const isLogged = isLoggedIn

Vue.use(Vuex);

export const store = new Vuex.Store({
    modules: {
      users,
      account,
      party,
    }
});