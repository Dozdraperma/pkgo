<template>
<div class="ListOfPoke">
  <section>
    <div class="SearchInput">
      <input type="text" v-model="InputName">
    </div>
  </section>
  <section>
  <div class="filter" >
    <button v-on:click="typ = !typ">Type</button>
    <button v-on:click="gener = !gener">Generation</button>
    <button v-on:click="legen = !legen">Legendary</button>
    <button v-on:click="rarly = !rarly">Rarly in pkgo</button>
    <div class="listtype" v-show="typ">
      <button @click="swap ('Normal')" class="POKEMON_TYPE_NORMAL">Normal</button>
      <button @click="swap ('Fighting')" class="POKEMON_TYPE_FIGHTING">Fighting</button>
      <button @click="swap ('Flying')" class="POKEMON_TYPE_FLYING">Flying</button>
      <button @click="swap ('Poison')" class="POKEMON_TYPE_POISON">Poison</button>
      <button @click="swap ('Ground')" class="POKEMON_TYPE_GROUND">Ground</button>
      <button @click="swap ('Rock')" class="POKEMON_TYPE_ROCK">Rock</button>
      <button @click="swap ('Bug')" class="POKEMON_TYPE_BUG">Bug</button>
      <button @click="swap ('Ghost')" class="POKEMON_TYPE_GHOST">Ghost</button>
      <button @click="swap ('Steel')" class="POKEMON_TYPE_STEEL">Steel</button>
      <button @click="swap ('Fire')" class="POKEMON_TYPE_FIRE">Fire</button>
      <button @click="swap ('Water')" class="POKEMON_TYPE_WATER">Water</button>
      <button @click="swap ('Grass')" class="POKEMON_TYPE_GRASS">Grass</button>
      <button @click="swap ('Electric')" class="POKEMON_TYPE_ELECTRIC">Electric</button>
      <button @click="swap ('Psychic')" class="POKEMON_TYPE_PSYCHIC">Psychic</button>
      <button @click="swap ('Ice')" class="POKEMON_TYPE_ICE">Ice</button>
      <button @click="swap ('Dragon')" class="POKEMON_TYPE_DRAGON">Dragon</button>
      <button @click="swap ('Dark')" class="POKEMON_TYPE_DARK">Dark</button>
    </div>
    <div class="listtype" v-show="gener"> next</div>
    <div class="listtype" v-show="legen">mewtwo mew lugia</div>
    <div class="listtype" v-show="rarly">mr. mime mr. rime sirfetch'd</div>
  </div>
  </section>
  <section>
  <div class="resolve">
    <div class="PokemonCart" v-for="item in FilteredPoke" :key="item">
      <div class="id">{{ item.id }}</div> <div class="imya">{{ item.name }}</div> <div class="primaryType">{{ item.primaryType }}</div> <div class="secondaryType">{{ item.secondaryType }}</div> <div class="MaxCP">MaxCP: {{  item.maxCP }}</div>
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
      type_sort: ''
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
  .SearchInput{
    margin: 20px 0;
  }
  .listtype {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    margin: 10px 0;
    button {
      color: white;
      text-shadow: 1px 1px #312f2f;
      border: none;
      width: 60px;
      padding: 2px 5px;
      margin: 0 2px;
      border-radius: 5px;
    }
  }
.PokemonCart{
  border: 2px solid gold;
  margin: 10px 50px;
  display: grid;
  grid-template-columns: 1fr 3fr 4fr 1fr;
  grid-template-rows: 20px 150px 20px;
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
    .PokemonCart{

    }
  }
}
</style>
