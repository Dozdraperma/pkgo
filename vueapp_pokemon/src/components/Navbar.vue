<template>
<div class="head">
  <img src="@/assets/pngkit_eevee-png_211496.png" alt='logo'>
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
.head {
  padding-top: 3px;
  background: #2c3e50;
}
</style>
