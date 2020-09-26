import Vue from 'vue';
import Vuex from 'vuex';
import VueRouter from 'vue-router';
import Login from '@/components/Login.vue';
import Dashboard from '@/components/Dashboard.vue';
import App from './App.vue';
import '@/assets/css/index.css';

Vue.config.productionTip = false;
Vue.use(VueRouter);
Vue.use(Vuex);

const store = new Vuex.Store({
  state: {
    token: '',
    authenticated: false,
  },
  getters: {
    getToken(state) {
      return state.token;
    },
    isAuthenticated(state) {
      return state.authenticated;
    },
  },
  mutations: {
    updateToken(state, newtoken) {
      state.token = newtoken;
      if (state.token !== '') {
        state.authenticated = true;
      }
    },
  },
});

export default {
  store,
};

const routes = [
  { path: '/login', component: Login },
  { path: '/dashboard', component: Dashboard },
];

const router = new VueRouter({
  routes,
});

new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount('#app');
