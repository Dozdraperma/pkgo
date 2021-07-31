<template>
<div class="ListOfPoke">
  <section>
    <div class="SearchInput">
      <input type="text" v-model="InputName" placeholder="Search">
    </div>
  </section>
  <section>
  <div class="filter" >
    <button v-on:click="typ = !typ">Type</button>
    <button v-on:click="gener = !gener">Generation</button>
    <button v-on:click="legen = !legen">Legendary</button>
    <button v-on:click="rarly = !rarly">Rarly in pkgo</button>
    <div class="listtype">
      <div class="tap" v-show="typ" v-for="tap in Typi" :key="tap">
        <button @click="swap (tap)" v-bind:class="'type POKEMON_TYPE_' + tap.toUpperCase()">{{ tap }}</button>
      </div>
    </div>
    <div class="listtype" v-show="gener"> next</div>
    <div class="listtype" v-show="legen">mewtwo mew lugia</div>
    <div class="listtype" v-show="rarly">mr. mime mr. rime sirfetch'd</div>
  </div>
  </section>
  <section>
  <div class="resolve">
    <div class="PokemonCart" v-for="item in FilteredPoke" :key="item">
      <div class="id">{{ item.id }}</div>
      <div class="imya">{{ item.name }}</div>
      <img :src="require(`../../src/views/media/Pokemon/pokemon_icon_${('1000' + item.id).slice(-3)}_00.png`)" alt="">
      <div v-bind:class="'type primaryType POKEMON_TYPE_' + item.primaryType.toUpperCase()">{{ item.primaryType }}</div>
      <div v-if="item.secondaryType" v-bind:class="'type secondaryType POKEMON_TYPE_' + item.secondaryType.toUpperCase()">{{ item.secondaryType }}</div>
      <div class="MaxCP">MaxCP: {{  item.maxCP }}</div>
    </div>
  </div>
  </section>
</div>
</template>

<script>
export default {
  name: 'ListPoke',
  data () {
    return {
      listPokemon: [],
      InputName: '',
      typ: false,
      gener: false,
      legen: false,
      rarly: false,
      type_sort: '',
      Typi: [
        'Normal',
        'Fire',
        'Water',
        'Grass',
        'Electric',
        'Ice',
        'Fighting',
        'Poison',
        'Ground',
        'Flying',
        'Psychic',
        'Bug',
        'Rock',
        'Dark',
        'Dragon',
        'Steel',
        'Ghost',
        'Fairy'
      ]
    }
  },
  methods: {
    swap (type) {
      this.type_sort === type ? this.type_sort = '' : this.type_sort = type
      console.log(this.type_sort)
    }
  },
  computed: {
    FilteredPoke: function () {
      const m = this.InputName
      const t = this.type_sort
      return this.listPokemon.filter(function (elem) {
        if (elem.name.toLowerCase().indexOf(m.toLowerCase()) > -1) {
          if (t !== '') {
            if (elem.secondaryType === t || elem.primaryType === t) return elem
          } else return elem
        }
      })
    }
  },
  created () {
    fetch('http://127.0.0.1:8000/api', {
      method: 'POST',
      mode: 'cors',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ query: '{searchPokemons(search: {name:""includeEvolutions:false}) {name, id, primaryType, secondaryType, maxCP}}' })
    }).then((response) => response.json())
      .then((json) => {
        for (let i = 0; i <= json.data.searchPokemons.length - 1; i++) {
          this.listPokemon.push(json.data.searchPokemons[i])
        }
      }).then(() => { console.log(this.listPokemon) })
  }
}
</script>

<style lang="scss" scoped>
.POKEMON_TYPE_NORMAL {
  background-color:#a8a878
}
.POKEMON_TYPE_FIRE {
  background-color:#f08030
}
.POKEMON_TYPE_WATER {
  background-color:#6890f0
}
.POKEMON_TYPE_GRASS {
  background-color:#78c850
}
.POKEMON_TYPE_POISON {
  background-color:#a040a0
}
.POKEMON_TYPE_ELECTRIC {
  background-color:#f8d030
}
.POKEMON_TYPE_GROUND {
  background-color:#e0c068
}
.POKEMON_TYPE_PSYCHIC {
  background-color:#f85888
}
.POKEMON_TYPE_ROCK {
  background-color:#b8a038
}
.POKEMON_TYPE_ICE {
  background-color:#98d8d8
}
.POKEMON_TYPE_BUG {
  background-color:#a8b820
}
.POKEMON_TYPE_DRAGON {
  background-color:#7038f8
}
.POKEMON_TYPE_GHOST {
  background-color:#705898
}
.POKEMON_TYPE_STEEL {
  background-color:#b8b8d0
}
.POKEMON_TYPE_FAIRY {
  background-color:#ee99ac
}
.POKEMON_TYPE_DARK {
  background-color: #312f2f
}
.POKEMON_TYPE_FLYING {
  background-color:#a890f0
}
.POKEMON_TYPE_FIGHTING {
  background-color:#c02038
}
.ListOfPoke {
  margin: 0 15%;
  .SearchInput{
    margin: 20px 0;
    input{
      width: 75%;
      height: 2em;
      font-size: 26px;
      text-align: center;
      font-family: "Roboto", "Lucida Grande", "DejaVu Sans", "Bitstream Vera Sans", Verdana, Arial, sans-serif;
      color: #312f2f;
      background-color: #d7ecef;
      border: 0;
      border-radius: 25px;
    }
  }
  .filter{
    background-color: #d7ecef;
  }
  .filter > button{
    background-color: #a4eff3;
    margin: 5px;
    border: 0;
    border-radius: 5px;
    padding: 5px 10px;
    font-family: "Roboto", "Lucida Grande", "DejaVu Sans", "Bitstream Vera Sans", Verdana, Arial, sans-serif;
  }

  .listtype {
    border-top: 1px solid rgba(0, 0, 0, 0.15);
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    margin: 0;
    button {
      margin: 0 2px;
    }
  }
  .type{
    color: white;
    text-shadow: 1px 1px #312f2f;
    border: none;
    width: 60px;
    padding: 2px 5px;
    border-radius: 5px;
  }
.PokemonCart{
  border: 2px solid gold;
  margin: 10px 5px;
  padding: 15px;
  display: grid;
  grid-template-columns: 1fr 3fr 4fr 1fr;
  grid-template-rows: 20px 150px 20px;
  align-items: center;
  .id{
    color: gray;
    grid-column-start: 1;
    grid-column-end: 2;
    grid-row: 1;
  }
  .id::before{
       content: '#';
  }
  .imya{
    grid-column-start: 2;
    grid-column-end: 5;
    grid-row: 1;
    color: #312f2f;
    font-size: 25px;
    font-weight: bold;
  }
  img{
    max-height: 100%;
    max-width: 100%;
    grid-column-start: 2;
    grid-column-end: 4;
    grid-row: 2;
    justify-self: center;
  }
  .primaryType{
    grid-column-start: 1;
    grid-column-end: 2;
    grid-row: 3;
  }
  .secondaryType{
    grid-column-start: 2;
    grid-column-end: 3;
    grid-row: 3;
  }
  .MaxCP{
    grid-column-start: 3;
    grid-column-end: 5;
    grid-row: 3;
  }
}
  .resolve{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 10px;
    margin: 20px;
  }
}
</style>
