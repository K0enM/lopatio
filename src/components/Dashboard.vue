<template>
  <div class="flex-col w-full md:flex md:flex-row md:min-h-screen">
    <div class="flex flex-col flex-shrink-0 w-full bg-blue-600 md:w-1/5">
      <div class="flex flex-row items-center justify-center flex-shrink-0 px-8 py-6">
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Dashboard',
  computed: {
    checkAuthentication: () => {
      if (!this.$store.getters.isAuthenticated) {
        this.$router.push('login');
      }
    },
    data() {
      return {
        authenticated: false,
      };
    },
  },
};
</script>

<style>

</style>
