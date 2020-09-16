<template>
  <header class="flex items-center justify-between px-4 py-3 bg-blue-600">
      <div>
          <h1 class="text-white font-semibold">'Lo Patio</h1>
      </div>
      <div>
          <button type="button"
          class="block text-white p-3 bg-green-500
            border-b-4 border-blue-800 focus:outline-none
            "><router-link to='login'>Huisgenoten Login</router-link></button>
      </div>
  </header>
</template>

<script>
export default {
  name: 'Navbar',
};
</script>

<style>

</style>
