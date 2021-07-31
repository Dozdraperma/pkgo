<template>
  <div class="side">
  <div class="PokemonBar">
    <PokemonSlot/>
    <PokemonSlot/>
    <PokemonSlot/>
  </div>
  </div>
</template>

<script>
import PokemonSlot from './PokemonSlot'
export default {
  name: 'Pokebar',
  components: { PokemonSlot }
}
</script>

<style lang="scss" scoped>
.side {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  grid-template-rows: 2fr max-content;
  .PokemonBar {
    grid-column: 1;
    grid-row: 2;
    display: grid;
    grid-template-columns: repeat(3, 33.3%);
    gap: 5px;
    background: #d7ecef;
    border-radius: 10px;
    box-shadow: 0 0 3px 3px rgba(7, 7, 7, .16);
  }
}
</style>
