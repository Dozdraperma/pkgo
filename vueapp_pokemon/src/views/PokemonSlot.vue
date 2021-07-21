<template>
<div class="PokemonSlot">
  <div class="remove"
       v-bind:style="{visibility: isVisibleinfo}"
       @click="onRemove"
></div>
  <p v-bind:style="{visibility: isVisibleinfo}">CP <span>{{ Pokemon.cp }}</span></p>
  <button
    v-on:click="openMenu"
  >
  </button>
  <p id="name" v-bind:style="{visibility: isVisibleinfo}">|{{ Pokemon.name }}|</p>
  <div class="PokemonMenu"
       v-bind:style="{ visibility: isVisible } "
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
      this.isVisibleinfo = 'visible'
    },
    openMenu () {
      this.isVisible === 'hidden' ? this.isVisible = 'visible' : this.isVisible = 'hidden'
    },
    onRemove () {
      this.Pokemon.id = ''
      this.Pokemon.name = ''
      this.Pokemon.cp = ''
      this.isVisibleinfo = 'hidden'
      this.sp = ''
      this.name = ''
    }
  },
  data () {
    return {
      Pokemon: { id: '', name: '', cp: '' },
      sp: '',
      name: '',
      isVisible: 'hidden',
      isVisibleinfo: 'hidden'
    }
  }
}
</script>

<style lang="scss" scoped>
.PokemonSlot{
  padding: 5px 5px;
  position: relative;
    button{
      border-radius: 10px;
      box-shadow: 0 0 5px 3px rgba(123, 161, 160, 0.2);
      padding: 30px;
      border: 2px solid #bad7db;
      background: linear-gradient(90deg, #ffffff ,#f7fdf3);
    }
    button:hover{
      box-shadow: 0 0 5px 7px rgba(123, 161, 160, 0.8);
      transition-duration: 200ms;
      }

  p {

    margin: 7px;
    font-size: 10px;
    font-weight: bold;
    span{
      font-size: 20px;
    }
  }

  #name {
    margin: 7px;
    font-size: 15px;
    font-weight: bold;
  }

  .PokemonMenu{
    visibility: hidden;
    z-index: 2;
    background: #ffffff;
    position: absolute;
    border-radius: 10px;
    padding: 5px;
    box-shadow: 0 0 5px 3px rgba(123, 161, 160, 0.3);
    button {
      padding: 2px 5px;
    }
  }
  form input {
    border-radius: 20px;
    border: none;
    background: #d7ecef;
    padding: 7px;
    text-align: center;
    margin: 5% 0;
    width: 70%;
  }
  .remove{
    opacity: 0;
    z-index: 4;
    background-image: url('media/free-icon-cross-black-circular-button-54473.svg');
    background-repeat: no-repeat;
    background-size: 50px 50px;
    background-position: center ;
    position:absolute;
    top: 39px;
    left: 15px;
    width: 70px;
    height: 70px;
  }
  .remove:hover{
    opacity: 0.5;
    transition-duration: 500ms;
  }
}
</style>
