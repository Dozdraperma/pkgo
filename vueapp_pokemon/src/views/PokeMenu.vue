<template>
  <div class="contan">
  <div class="PokemonMenu"
       v-bind:style="{ visibility: isVisibl } "
  >
    <form @submit.prevent="onSubmit">
      <input type="text" placeholder="Имя" v-model="name">
      <div class="wrappy">
        <div class="search" v-show="vis">
          <button  @click="ekanS (item.name)" v-for="item in listPokemon" :key="item">{{ item.name }}</button>
        </div>
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
    ekanS (item) {
      this.name = item
    },
    onSubmit () {
      if (this.sp > 9) {
        this.$emit('onsubmit', {
          name: this.name,
          sp: this.sp
        })
      }
    }
  },
  watch: {
    name: function (name) {
      const data = { query: `{searchPokemons(search: {name:"${name}"includeEvolutions:false}) {name}}` }
      if (name) {
        this.vis = false
        this.listPokemon = []
        fetch('http://127.0.0.1:8000/api', {
          method: 'POST',
          mode: 'cors',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(data)
        }).then((response) => response.json())
          .then((json) => {
            if (json.data.searchPokemons !== null && !(json.data.searchPokemons.length === 1 && json.data.searchPokemons[0].name.toLowerCase() === name.toLowerCase())) {
              for (let i = 0; i <= json.data.searchPokemons.length - 1; i++) {
                this.listPokemon.push(json.data.searchPokemons[i])
              }
              this.vis = true
            }
          })
      } else { this.listPokemon = []; this.vis = false }
    }
  },
  data () {
    return {
      Pokemon: { id: '', name: '', cp: '' },
      sp: '',
      name: '',
      listPokemon: [],
      vis: false
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
  form {
    .wrappy {
      display: flex;
      justify-content: center;
      position: relative;
      .search {
        background-color: #2c3e50;
        display: flex;
        flex-direction: column;
        position: absolute;
        height: 184px;
        width: 86%;
        overflow-y: scroll;
        transform: translateX(4%);
      }
    }
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
