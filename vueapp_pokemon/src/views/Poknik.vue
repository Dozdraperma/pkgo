<template>
  <div class="TOMACH">
    <h1> Эта страница посвящена покемону {{ DataPokemon.name }}</h1>
    <img v-if="DataPokemon.id" :src="require(`../../src/views/media/Pokemon/pokemon_icon_${('1000' + DataPokemon.id).slice(-3)}_00.png`)" alt="ponk">
    {{ DataPokemon }}
  </div>
</template>

<script>
export default {
  name: 'Poknik',
  data () {
    return {
      DataPokemon: {}
    }
  },
  created () {
    fetch('http://127.0.0.1:8000/api', {
      method: 'POST',
      mode: 'cors',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ query: `{getPokemon(id:${this.$route.params.Poknik}) {name, id, height, weight, maxCP, baseAttack, baseDefense, baseStamina, primaryType, secondaryType}}` })
    }).then((response) => response.json())
      .then((json) => { this.DataPokemon = json.data.getPokemon })
  }

}

</script>

<style scoped>

</style>
