<template>
  <header class="flex items-center justify-between px-4 py-3 bg-blue-600">
      <div>
          <h1 class="text-white font-semibold text-lg tracking-wider">'Lo Patio</h1>
      </div>
      <div>
          <button type="button"
          class="block text-white p-3 bg-green-500
            border-b-4 border-blue-800 focus:outline-none
            "><router-link to='login'>Huisgenoten Login</router-link></button>

            <button type="button"
          class="block text-white p-3 bg-green-500
            border-b-4 border-blue-800 focus:outline-none"
            v-if="authenticated" @click="logOut()">Uitloggen</button>
      </div>
  </header>
</template>

<script>
import { mapGetters } from 'vuex';
import axios from 'axios';

export default {
  name: 'Navbar',
  computed: {
    ...mapGetters({ authenticated: 'isAuthenticated', token: 'getToken' }),
  },
  updated() {
    /* eslint-disable no-unused-vars */
    this.api = axios.create({
      baseURL: 'http://localhost:8080/api/',
      xsrfCookieName: 'csrftoken',
      headers: {
        'Authorization': `Token ${this.token}`,
      },
    });
    /* eslint-enable no-unused-vars */
  },
  data() {
    return {
      api: null,
    };
  },
  methods: {
    rerouteToLogin: function () {
      this.$router.push('login');
    },
    logOut: function () {
      this.api.post('/auth/logout/').then(function (response) {
        if (response.status === 204) {
          this.rerouteToLogin();
        }
      });
    },
  },
};
</script>

<style>

</style>
