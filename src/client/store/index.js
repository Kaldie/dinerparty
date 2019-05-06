import Vue from 'vue';
import Vuex from 'vuex';

// import { alert } from './alert.module';
import { user } from './user';
// import { users } from './users.module';

Vue.use(Vuex);

export const store = new Vuex.Store({
    modules: {
      user,
    }
});