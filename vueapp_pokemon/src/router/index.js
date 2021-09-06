import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/About',
    name: 'About',
    component: () => import('../views/About.vue')
  },
  {
    path: '/Battles',
    name: 'Battles',
    component: () => import('../views/Battles.vue')
  },
  {
    path: '/ListPoke',
    name: 'ListPoke',
    component: () => import('../views/ListPoke.vue')
  },
  {
    path: 'ListPoke/:Poknik',
    name: 'Poknik',
    component: () => import('../views/Poknik.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
