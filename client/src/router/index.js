import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Menu',
    component: () => import('@/views/Menu.vue')
  },
  {
    path: '/chess/:address/:port',
    name: 'Game',
    component: () => import('@/views/Game.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
