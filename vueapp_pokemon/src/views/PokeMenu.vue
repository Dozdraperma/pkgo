<template>
  <div class="Container">
    <div class="PokemonMenu" v-bind:style="{ visibility: MenuVisible }">
      <form @submit.prevent="onSubmit">
        <input type="text" placeholder="Имя" v-model="name" >
        <div class="wrappy">
          <div class="search" v-if="name && listPokemon.length !== 0 && name.toUpperCase() !== listPokemon[0].name.toUpperCase()">
            <button  @click="ekanS (Pokemon)" v-for="Pokemon in listPokemon" :key="Pokemon.name">{{ Pokemon.name }}</button>
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
import gql from 'graphql-tag'

const QueryName = gql`query($name: String){ getPokemons(input: {filter: {name: $name}}) {name} }`

export default {
  props: ['MenuVisible'],
  name: 'PokeMenu',
  apollo: {
    NameHint: {
      query: QueryName,
      variables () {
        return {
          name: this.name
        }
      },
      skip () {
        return this.skipQuery
      },
      debounce: 500,
      update: data => data.NameHint,
      result (data) { this.listPokemon = data.data.getPokemons }
    }
  },
  methods: {
    ekanS (item) {
      this.name = item.name
    },
    onSubmit () {
      this.$emit('onsubmit', {
        name: this.name,
        sp: this.sp
      })
    }
  },
  watch: {
    name: function (name) {
      name ? this.$apollo.queries.NameHint.skip = false : this.$apollo.queries.NameHint.skip = true
    }
  },
  data () {
    return {
      Pokemon: { id: '', name: '', cp: '' },
      sp: '',
      name: '',
      listPokemon: []
    }
  }
}
</script>

<style lang="scss" scoped>
.Container{
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
