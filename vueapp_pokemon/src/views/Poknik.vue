<template>
  <div class="InfoPokemon">
    <h1> Эта страница посвящена покемону {{ DataPokemon.name }}</h1>
    <img v-if="DataPokemon.id" :src="require(`../../src/views/media/Pokemon/pokemon_icon_${('1000' + DataPokemon.id).slice(-3)}_00.png`)" alt="ponk">
    {{ DataPokemon }}
  </div>
</template>

<script>
import gql from 'graphql-tag'

export default {
  name: 'Poknik',
  apollo: {
    QueryAllInfo: {
      query: gql`query ($Bars: ID!){getPokemon(id: $Bars) {id, name, secondaryType, primaryType, maxCP, baseAttack, baseDefense, baseStamina, familyName}}`,
      variables () {
        return {
          Bars: this.idPokemon
        }
      },
      update: data => data.QueryAllInfo,
      result (data) { this.DataPokemon = data.data.getPokemon }
    }
  },
  data () {
    return {
      idPokemon: this.$route.params.Poknik,
      DataPokemon: {}
    }
  }
}

</script>

<style scoped>

</style>
