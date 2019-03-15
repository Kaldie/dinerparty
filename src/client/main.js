import Vue from 'vue'
import VueRouter from 'vue-router'
import myRouter from '@/client/router'
import App from '@/client/components/App'

import '@/client/utilities/FontAwesome'

import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import '@/client/utilities/FontAwesome'

Vue.config.productionTip = false
Vue.use(BootstrapVue)
Vue.use(VueRouter)

new Vue({
  router: myRouter,
  render: h => h(App),
}).$mount('#app')
