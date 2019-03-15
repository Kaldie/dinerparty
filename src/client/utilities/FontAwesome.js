import { library } from '@fortawesome/fontawesome-svg-core'
import { faCoffee, faCalendar } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import Vue from 'vue'

library.add(faCoffee, faCalendar)
Vue.component('font-awesome-icon', FontAwesomeIcon)