<template>
  <div class="PokemonBar">
    <PokemonSlot/>
    <PokemonSlot/>
    <PokemonSlot/>
  </div>
</template>

<script>
import PokemonSlot from './PokemonSlot'
export default {
  name: 'Pokebar',
  components: { PokemonSlot }
}
</script>

<style scoped>
.PokemonBar{
  display: grid;
  grid-template-columns: repeat(3,100px);
  gap: 5px;
  background: #d7ecef;
  border-radius: 10px;
  box-shadow: 0 0 3px 3px rgba(7, 7, 7, .16);
}
</style>
