<template>
<div class="PokemonSlot">
  <p v-if="Pokemon.cp">CP <span>{{ Pokemon.cp }}</span></p>
  <button
    v-on:click="openMenu"
  >
  </button>
  <p>{{ Pokemon.name }}</p>
  <div class="PokemonMenu"
       v-show="isVisible"
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
  name: 'PokemonSlot',
  methods: {
    onSubmit () {
      this.Pokemon.id = Date.now()
      this.Pokemon.name = this.name
      this.Pokemon.cp = this.sp
    },
    openMenu () {
      this.isVisible = !this.isVisible
    }
  },
  data () {
    return {
      Pokemon: { id: '', name: '', cp: '' },
      sp: '',
      name: '',
      isVisible: false
    }
  }
}
</script>

<style scoped>
.PokemonSlot{
  padding: 5px 5px;
  position: relative;
  background-image: url("C:Users/Dan/All project/pkgo/vueapp_pokemon/src/assets/pokeball.svg");
}
.PokemonSlot button{
  border-radius: 10px;
  box-shadow: 0 0 5px 3px rgba(123, 161, 160, 0.2);
  padding: 30px;
  border: 2px solid #bad7db;
  background: linear-gradient(90deg, #ffffff ,#f7fdf3);
}
.PokemonSlot button:hover{
  box-shadow: 0 0 5px 7px rgba(123, 161, 160, 0.8);
  transition-duration: 200ms;
}
p {
  margin: 7px;
}
.PokemonSlot .PokemonMenu{
  z-index: 2;
  background: #ffffff;
  position: absolute;
  border-radius: 10px;
  padding: 5px;
  box-shadow: 0 0 5px 3px rgba(123, 161, 160, 0.3);
}
.PokemonSlot .PokemonMenu button {
  padding: 2px 5px;
}
.PokemonSlot .PokemonMenu form input {
  border-radius: 20px;
  border: none;
  background: #d7ecef;
  padding: 7px;
  text-align: center;
  margin: 5% 0;
  width: 70%;
}
</style>
