<template>
  <div id="app">
  <Navbar />
  <router-view/>
  </div>
</template>

<script>
import Navbar from './components/Navbar'
export default {

  components: { Navbar }
}
</script>

<style lang="scss">
body{
  margin: 0;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  text-align: center;
  color: #2c3e50;
}
</style>
