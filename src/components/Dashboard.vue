<template>
  
</template>

<script>
export default {
  name: 'Dashboard',
  beforeMount: () => {
    if (this.$store.state.token == '') {
      this.$router.push('login')
    }
  }
}
</script>

<style>

</style>