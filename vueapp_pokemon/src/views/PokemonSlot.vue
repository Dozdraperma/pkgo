<template>
<div class="PokemonSlot" >
  <div class="wRap">
    <div class="remove"
         v-bind:style="{visibility: isVisibleinfo}"
         @click="onRemove">
    </div>
  </div>
    <p v-bind:style="{visibility: isVisibleinfo}">CP <span>{{ Pokemon.cp }}</span></p>
    <button v-on:click="openMenu">
      <img v-if="Pokemon.id" :src="require(`../../src/views/media/Pokemon/pokemon_icon_${('1000' + Pokemon.id).slice(-3)}_00.png`)" alt="">
    </button>
    <p id="name" v-bind:style="{visibility: isVisibleinfo}">|{{ Pokemon.name }}|</p>
  <PokeMenu v-bind:isVisibl="isVisible"
            v-on:onsubmit="onSubmit"
  />
  </div>
</template>

<script>
import PokeMenu from './PokeMenu'
export default {
  name: 'PokemonSlot',
  components: { PokeMenu },
  methods: {
    openMenu () {
      this.isVisible === 'hidden' ? this.isVisible = 'visible' : this.isVisible = 'hidden'
    },
    onSubmit (ab) {
      fetch('http://127.0.0.1:8000/api', {
        method: 'POST',
        mode: 'cors',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ query: `{searchPokemons(search: {name:"${ab.name}"includeEvolutions:false}) {id}}` })
      }).then((response) => response.json())
        .then((json) => { this.Pokemon.id = json.data.searchPokemons[0].id })
      this.Pokemon.name = ab.name
      this.Pokemon.cp = ab.sp
      this.isVisibleinfo = 'visible'
    },
    onRemove () {
      this.Pokemon.id = ''
      this.Pokemon.name = ''
      this.Pokemon.cp = ''
      this.isVisibleinfo = 'hidden'
    }
  },
  data () {
    return {
      Pokemon: { id: '', name: '', cp: '' },
      isVisible: 'hidden',
      isVisibleinfo: 'hidden'
    }
  }
}
</script>

<style lang="scss" scoped>
.PokemonSlot {
  font-family: "Montserrat", "Helvetica", "Roboto", sans-serif;
  padding: 5px 5px;
  position: relative;
  img{
    max-width: 100%;
    max-height: 50%;
  }
  p {
    margin: 7px;
    font-size: 10px;
    font-weight: bold;

    span {
      font-size: 20px;
    }
  }
  #name {
    margin: 7px;
    font-size: 15px;
    font-weight: bold;
  }

  button {
    border-radius: 10px;
    box-shadow: 0 0 5px 3px rgba(123, 161, 160, 0.2);
    width: 70px;
    height: 70px;
    border: 2px solid #bad7db;
    background: linear-gradient(90deg, #ffffff, #f7fdf3);
  }

  button:hover {
    box-shadow: 0 0 5px 7px rgba(123, 161, 160, 0.8);
    transition-duration: 200ms;
  }
  .wRap {
    position: relative;
    display: flex;
    justify-content: center;
    .remove {
      opacity: 0;
      z-index: 4;
      background-image: url('media/free-icon-cross-black-circular-button-54473.svg');
      background-repeat: no-repeat;
      background-size: 50px 50px;
      background-position: center;
      position: absolute;
      top: 37px;
      width: 70px;
      height: 70px;
    }
    .remove:hover {
      opacity: 0.5;
      transition-duration: 500ms;
    }
  }
}
</style>
