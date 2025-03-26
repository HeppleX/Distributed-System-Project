import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    redirect: '/login'
  },
  {
    path: '/login',
    name: 'Login',
    component: () => import('../views/Login'),
    meta: {
        title: "Login"
    }
  },
  {
    path: '/home',
    name: 'Home',
    component: () => import('../views/Home'),
    redirect: '/home/personal',
    meta: {
        title: "Home"
    },
    children: [
      {
        path: 'personal',
        name: 'Personal',
        component: () => import('../views/Home/Personal'),
        meta: {
            title: "Personal"
        },
      },
      {
        path: 'list',
        name: 'List',
        component: () => import('../views/Home/List'),
        meta: {
            title: "List"
        },
      }
    ]
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
