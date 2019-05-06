import VueRouter from 'vue-router'
import Home from '@/client/components/Home'
import ShowParties from '@/client/components/parties/Parties'
import Host from '@/client/components/Host'
import Profile from '@/client/components/Profile'
import Login from '@/client/components/Login'

const routes = [
  { path: '/' , component: Home},
  { path: '/find' , component: ShowParties},
  { path: '/host' , component: Host},
  { path: '/profile', component: Profile },
  { path: '/login', component: Login}
]

const router = new VueRouter({
  mode: 'history',
  routes
})

router.beforeEach((to, from, next) => {
  // redirect to login page if not logged in and trying to access a restricted page
  const publicPages = ['/find', '/', '/host', '/login'];
  const authRequired = !publicPages.includes(to.path)
  if ( authRequired ) {
    return next('/login');
  }
  next();
})


export default router