import VueRouter from 'vue-router'
import Home from '@/client/components/Home'
import ShowParties from '@/client/components/parties/Parties'
import Host from '@/client/components/Host'
import Profile from '@/client/components/Profile.vue'

const routes = [
  { path: '/' , component: Home},
  { path: '/find' , component: ShowParties},
  { path: '/host' , component: Host},
  { path: '/profile', component: Profile },
]

const router = new VueRouter({
  routes
})

export default router