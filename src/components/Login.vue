<template>
  <div class="flex justify-center items-center h-screen w-full">
    <div class="w-full max-w-xs">
    <form class="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4">
      <div class="mb-4">
        <label class="block text-gray-700 text-sm font-bold mb-2" for="username">Username</label>
        <input
          class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
          id="username"
          type="text"
          placeholder="Username" v-model="username"
        />
      </div>
      <div class="mb-6">
        <label class="block text-gray-700 text-sm font-bold mb-2" for="password">Password</label>
        <input
          class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline"
          id="password"
          type="password" v-model="password"
          placeholder="******************"
        />
      </div>
      <div class="flex items-center justify-between">
        <button
          class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
          type="button" v-on:click="doLogin()"
        >Sign In</button>
      </div>
    </form>
    <p class="text-center text-gray-500 text-xs">&copy;2020 'Lo Patio</p>
  </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Login',
  mounted() {
    /* eslint-disable no-unused-vars */
    this.api = axios.create({
      baseURL: 'http://localhost:8080/api/',
      xsrfCookieName: 'csrftoken',
    });
    /* eslint-enable no-unused-vars */
  },
  data() {
    return {
      username: '',
      password: '',
      api: null,
    };
  },
  methods: {
    doLogin() {
      this.api.post('/auth/login/', {
        username: this.username,
        password: this.password,
      }).then((response) => {
        this.$store.commit('updateToken', response.data.token);
        this.$router.push('dashboard');
      }).catch((error) => {
        if (error.response) {
          console.log(error.response.data);
          console.log(error.response.status);
          console.log(error.response.headers);
        }
      });
    },
  },
};
</script>

<style>
</style>
