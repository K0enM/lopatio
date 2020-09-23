import Vue from 'vue';
import Vuex from 'vuex';
import VueRouter from 'vue-router';
import Login from '@/components/Login.vue';
import App from './App.vue';
import '@/assets/css/index.css';

Vue.config.productionTip = false;
Vue.use(VueRouter);
Vue.use(Vuex);

const store = new Vuex.Store({
  state: {
    token: '',
  },
  getters: {
    getToken: (state) => state.token,
  },
  mutations: {
    updateToken(state, newtoken) {
      state.token = newtoken;
    },
  },
});

const routes = [
  { path: '/login', component: Login },
];

const router = new VueRouter({
  routes,
});

new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount('#app');
