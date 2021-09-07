<template>
  <div class="InfoPokemon">
    <h1> Эта страница посвящена покемону {{ DataPokemon.name }}</h1>
    <header>
      <img v-if="DataPokemon.id" :src="require(`../../src/views/media/Pokemon/pokemon_icon_${('1000' + DataPokemon.id).slice(-3)}_00.png`)" alt="ponk">
      <h2>{{DataPokemon.id}}</h2>
    </header>
    <div>
      <h3>Тип покемона</h3>
      {{DataPokemon.primaryType}}
      {{DataPokemon.secondaryType}}
    </div>
    <div>
      {{DataPokemon.baseAttack}}
      {{DataPokemon.baseStamina}}
      {{DataPokemon.baseDefense}}
    </div>
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
          Bars: this.$route.path.slice(10)
        }
      },
      update: data => data.QueryAllInfo,
      result (data) { this.DataPokemon = data.data.getPokemon }
    }
  },
  data () {
    return {
      DataPokemon: {}
    }
  }
}

</script>

<style scoped>

</style>
