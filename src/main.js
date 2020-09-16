import Vue from 'vue';
import VueRouter from 'vue-router';
import Login from '@/components/Login.vue';
import App from './App.vue';
import '@/assets/css/index.css';

Vue.config.productionTip = false;
Vue.use(VueRouter);

const routes = [
  { path: '/login', component: Login },
];

const router = new VueRouter({
  routes,
});

new Vue({
  router,
  render: (h) => h(App),
}).$mount('#app');
