import Vue from 'vue'
import VueRouter from 'vue-router'
import VeeValidate from 'vee-validate'

import myRouter from '@/client/router'
import App from '@/client/components/App'
import { store }  from '@/client/store'

import '@/client/utilities/FontAwesome'
import '@/client/utilities/FontAwesome'

Vue.config.productionTip = false
Vue.use(VueRouter)
Vue.use(VeeValidate);

new Vue({
  router: myRouter,
  store,
  render: h => h(App),
}).$mount('#app')
