<template>
  <div class="PokemonSlot" >
    <div class="remove"
         v-bind:style="{visibility: isVisibleinfo}"
         @click="onRemove"></div>
    <p v-bind:style="{visibility: isVisibleinfo}">CP <span>{{ Pokemon.cp }}</span></p>
    <button v-on:click="openMenu">
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
      this.Pokemon.id = Date.now()
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
    padding: 30px;
    border: 2px solid #bad7db;
    background: linear-gradient(90deg, #ffffff, #f7fdf3);
  }
  button:hover {
    box-shadow: 0 0 5px 7px rgba(123, 161, 160, 0.8);
    transition-duration: 200ms;
  }
  .remove {
    opacity: 0;
    z-index: 4;
    background-image: url('media/free-icon-cross-black-circular-button-54473.svg');
    background-repeat: no-repeat;
    background-size: 50px 50px;
    background-position: center;
    position: absolute;
    top: 39px;
    left: 15px;
    width: 70px;
    height: 70px;
  }
  .remove:hover {
    opacity: 0.5;
    transition-duration: 500ms;
  }
}
</style>
