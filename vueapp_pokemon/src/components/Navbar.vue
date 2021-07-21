<template>
<div>
  <img src="@/assets/logo.png" alt='logo'>
  <Links />
</div>
</template>

<script>
import Links from './Links'
export default {
  name: 'Navbar',
  components: { Links }
}
</script>

<style scoped>
div {
  background: #38a6eb;
}
</style>
