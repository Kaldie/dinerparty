import Vue from 'vue';
import Vuex from 'vuex';

// import { alert } from './alert.module';
import { users } from './users';
import { account, isLoggedIn } from './account';

export const isLogged = isLoggedIn

Vue.use(Vuex);

export const store = new Vuex.Store({
    modules: {
      users,
      account
    }
});