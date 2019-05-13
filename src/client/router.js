import VueRouter from 'vue-router'
import Home from '@/client/components/Home'
import ShowParties from '@/client/components/parties/Parties'
import Host from '@/client/components/Host'
import Profile from '@/client/components/Profile'
import Login from '@/client/components/Login'
import Register from '@/client/components/Register'
import { isLogged } from '@/client/store'

const routes = [
  { path: '/' , component: Home},
  { path: '/find' , component: ShowParties},
  { path: '/host' , component: Host},
  { path: '/profile', component: Profile },
  { path: '/login', component: Login},
  { path: '/register', component: Register}
]

const router = new VueRouter({
  mode: 'history',
  routes
})

router.beforeEach((to, from, next) => {
  // redirect to login page if not logged in and trying to access a restricted page
  const publicPages = ['/find', '/', '/host', '/login', '/register'];
  const authRequired = !publicPages.includes(to.path)

  console.warn("isLogged()", isLogged())

  if ( authRequired && !isLogged() ) {
    return next('/login');
  }
  next();
})


export default router