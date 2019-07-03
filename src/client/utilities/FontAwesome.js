import { library } from '@fortawesome/fontawesome-svg-core'
import { faCoffee, faCalendar, faHome, faBell, faUtensils, faIdBadge, faSignInAlt, faSignOutAlt} from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import Vue from 'vue'

library.add(faCoffee, faCalendar, faHome, faBell, faUtensils, faIdBadge, faSignInAlt, faSignOutAlt)
Vue.component('font-awesome-icon', FontAwesomeIcon)