<template>
<div class="links">
  <router-link to="/">Home</router-link>
  <router-link to="/About">About</router-link>
  <router-link to="/Battles">Battles</router-link>
  <router-link to="/ListPoke">List of Pokemon</router-link>
</div>
</template>

<script>
export default {
  name: 'Links'
}
</script>

<style lang="scss" scoped>
.links{
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  flex-direction: row;
  align-self: end;
    a {
      background-color: #2c3e50;
      padding: 20px 0;
      text-decoration: none;
      color: white;
      font-size: 30px;
      font-family: "Roboto", "Helvetica", "Roboto", sans-serif;
      font-weight: normal;
    }
  :hover{
    background-color: #d7ecef;
    color: #2c3e50;
    transition-duration: 0.2s;
  }
}

</style>
