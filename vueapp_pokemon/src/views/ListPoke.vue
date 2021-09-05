<template>
<div class="ListOfPoke" >
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
    <div class="listtype" v-show="typ">
      <button @click="swap (tap, index)" v-bind:class="`type POKEMON_TYPE_${tap.toUpperCase()}`" v-for="(tap, index) in Typi" :key="tap">{{ tap }}</button>
    </div>
    <div class="gener" v-show="gener">
      <button v-for="(gener) in geners" :key="gener">{{ gener }}</button>
    </div>
    <div class="listtyp" v-show="legen">mewtwo mew lugia</div>
    <div class="listtyp" v-show="rarly">mr. mime mr. rime sirfetch'd</div>
  </div>
  </section>
  <section>
  <div class="resolve">
    <router-link :to="{ name: 'Poknik', params: { Poknik: item.id }}" class="PokemonCart" v-for="item in listPokemon" :key="item.id">
      <div class="id">{{ item.id }}</div>
      <div class="imya">{{ item.name }}</div>
      <img :src="require(`../../src/views/media/Pokemon/pokemon_icon_${('1000' + item.id).slice(-3)}_00.png`)" alt="">
      <div v-bind:class="`type primaryType POKEMON_TYPE_${item.primaryType.toUpperCase()}`">{{ item.primaryType }}</div>
      <div v-if="item.secondaryType" v-bind:class="`type secondaryType POKEMON_TYPE_${item.secondaryType.toUpperCase()}`">{{ item.secondaryType }}</div>
      <div class="MaxCP">MaxCP: {{  item.maxCP }}</div>
    </router-link>
  </div>
  </section>
</div>
</template>

<script>
import gql from 'graphql-tag'

export default {
  name: 'ListPoke',
  data () {
    return {
      borderis: '1px solid gray',
      listPokemon: [],
      InputName: '',
      typ: false,
      gener: false,
      legen: false,
      rarly: false,
      type_sort: '',
      offset: 0,
      geners: [
        'Канто (1)',
        'Джото (2)',
        'Хоэнн (3)',
        'Синно (4)',
        'Юнова (5)',
        'Калос (6)',
        'Алола (7)',
        'Галар (8)'
      ],
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
  apollo: {
    FetchListPoke: {
      query: gql`query($offset: Int!, $limit: Int!){getPokemons(input: {pagination: {offset: $offset limit: $limit}}) {id, name, primaryType, secondaryType, maxCP}}`,
      variables () {
        return {
          offset: this.offset,
          limit: 15
        }
      },
      update: data => data.listPokemon,
      result (data) {
        this.listPokemon = this.listPokemon.concat(data.data.getPokemons)
      }
    }
  },
  methods: {
    swap (type, index) {
      if (this.type_sort === type) {
        this.type_sort = ''
        document.querySelector('.listtype').children[index].classList.remove('active')
      } else {
        if (this.type_sort !== '') {
          document.querySelector('.active').classList.remove('active')
        }
        this.type_sort = type
        document.querySelector('.listtype').children[index].classList.add('active')
      }
    },
    Kebov () {
      if (window.scrollY + document.documentElement.clientHeight >= document.documentElement.scrollHeight - 50) {
        this.offset += 15
      }
    }
  },

  created () {
    window.addEventListener('scroll', this.Kebov)
  },
  unmounted () {
    window.removeEventListener('scroll', this.Kebov)
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
      width: 100%;
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
    color: #312f2f;
    background-color: inherit;
    margin: 5px;
    border: 1px solid #7e8587;
    border-radius: 5px;
    padding: 5px 10px;
    font-family: "Montserrat", Verdana, Arial, sans-serif;
    }
    .filter > button:hover{
      background-color: #2c3e50;
      color: white;
      transition-duration: 0.1s;
  }

  .listtype {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    margin: 0;

    .active {
       border: 2px solid red;
     }
    button:hover{
       background-color: #b8b8d0;
       transition-duration: 0.2s;
     }
  }
  .type{
    margin: 2px;
    color: white;
    text-shadow: 1px 1px #312f2f;
    border: 2px solid rgba(0, 0, 0, 0);
    width: 60px;
    padding: 2px 5px;
    border-radius: 5px;
  }
.PokemonCart{
  background: #fffefa;
  text-decoration: none;
  border: 4px solid #312f2f;

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
    color: #312f2f;
  }
}
  .PokemonCart:hover{
    background: #d7ecef;
    transition-duration: .1s;
}
  .resolve{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 10px;
    margin: 20px;
  }
}
</style>
