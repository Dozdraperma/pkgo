<template>
<div class="links">
  <router-link to="/">Home</router-link>
  <router-link to="/About">About</router-link>
  <router-link to="/Battles">Battles</router-link>
</div>
</template>

<script>
export default {
  name: 'Links'
}
</script>

<style scoped>
.links{
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  align-self: end;
}
a {
  text-decoration: none;
  color: #2c3e50;
  font-size: 30px;
  font-family: "Montserrat", "Helvetica", "Roboto", sans-serif;
  font-weight: bold;
}
a:hover{
  transform: scale(1.2);
  transition-duration: 100ms;
}
</style>
