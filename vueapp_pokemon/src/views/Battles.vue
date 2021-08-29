<template>
  <div class="Battles">
    <div class="hero">
      <Pokebar/>
    </div>
    <div class="opponent">
      <Pokebar/>
    </div>
  </div>
</template>

<script>
import Pokebar from './Pokebar'
export default {
  name: 'Battles',
  components: { Pokebar }
}
</script>

<style lang="scss" scoped>
.Battles{
  margin: 0 10%;
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-template-rows: 400px max-content;
  .hero{
    grid-column: 1;
    grid-row: 2;
  }
  .opponent{
    grid-column: 3;
    grid-row: 2;
  }
}
</style>
