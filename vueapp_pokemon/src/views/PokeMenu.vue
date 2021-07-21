<template>
  <div class="contan">
  <div class="PokemonMenu"
       v-bind:style="{ visibility: isVisibl } "
  >
    <form @submit.prevent="onSubmit">
      <input type="text" placeholder="Имя" v-model="name">
      <input type="text" placeholder="СР" maxlength="4" v-model="sp">
      <button type="submit">Добавить</button>
    </form>
  </div>
  </div>
</template>

<script>
export default {
  props: ['isVisibl'],
  name: 'PokeMenu',
  methods: {
    onSubmit () {
      this.$emit('onsubmit', {
        name: this.name,
        sp: this.sp
      })
    }
  },
  data () {
    return {
      Pokemon: { id: '', name: '', cp: '' },
      sp: '',
      name: ''
    }
  }
}
</script>

<style lang="scss" scoped>
.contan{
  display: flex;
  justify-content: center;
  position: relative;
}
.PokemonMenu {
  visibility: hidden;
  z-index: 2;
  background: #ffffff;
  position: absolute;
  margin: 0 20%;
  border-radius: 10px;
  padding: 5px;
  box-shadow: 0 0 5px 3px rgba(123, 161, 160, 0.3);
  width: 100%;

form input {
  border-radius: 20px;
  border: none;
  background: #d7ecef;
  padding: 7px;
  text-align: center;
  margin: 5% 0;
  width: 70%;
}

button {
  padding: 2px 5px;
}
}
</style>
