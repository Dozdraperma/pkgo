<template>
  <div>
    <h1>Home page</h1>
    {{ hello }}
    <p>This is home page. Our site was created to learn pokemons, computed the chances of battles and, of course, 'cause of <strong>great love</strong> for pokemon</p>
  </div>
</template>

<script>
import gql from 'graphql-tag'
export default {
  name: 'Home',
  apollo: {
    hello: gql`query { hello }`
  }
}
</script>

<style scoped>

</style>
