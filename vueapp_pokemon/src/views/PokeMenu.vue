<template>
  <div class="contan">
  <div class="PokemonMenu"
       v-bind:style="{ visibility: isVisibl } "
  >
    <form @submit.prevent="onSubmit">
      <input type="text" placeholder="Имя" v-model="name" >
      <div class="search" v-for="item in items" :key="item">
        {{ item }}
      </div>
      <input type="text" placeholder="СР" maxlength="4" v-model="sp">
      <br>
      <button type="submit">ДОБАВИТЬ</button>
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
  watch: {
    name: function (name) {
      const fet = '{searchPokemons(search: {name: {name:"' + name + '" includeEvolutions:true}}) {name}}'
      console.log(fet)
      fetch('http://127.0.0.1:8000/api', {
        method: 'POST',
        mode: 'cors',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(fet.value)
      }).then((response) => response.json()).then((json) => console.log(json))
    }
  },
  data () {
    return {
      Pokemon: { id: '', name: '', cp: '' },
      sp: '',
      name: '',
      pokemonser: ''
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
  font-family: "Montserrat", "Helvetica", "Roboto", sans-serif;
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
  font-family: "Montserrat", "Helvetica", "Roboto", sans-serif;
  border-radius: 20px;
  border: none;
  background: #d7ecef;
  padding: 7px;
  text-align: center;
  margin: 5px 0;
  width: 70%;
}

button {
  font-family: 'Encode Sans SC', "Helvetica", "Roboto", sans-serif;
  padding: 4px 9px;
  margin-top: 5px;
  font-weight: 600;
  background-color: #38a6eb;
  color: #2c3e50;
  border: 0;
  border-radius: 15px;
}
}
</style>
