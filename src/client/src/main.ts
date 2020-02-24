import Vue from 'vue';
import { OvermindPlugin } from './store';
import App from './App.vue';
import router from './router';
import vuetify from '@/plugins/vuetify'; // path to vuetify export

Vue.use(OvermindPlugin);

Vue.config.productionTip = false;

new Vue({
  vuetify,
  router,
  render: (h) => h(App),
}).$mount('#app');
