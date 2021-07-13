function EventOnPokeball() {
  let NumberBall = document.querySelector(".PokemonBar button").getAttribute('ClassName')
}

for (let elem of document.querySelectorAll("div.PokemonBar > button")){
  elem.addEventListener("focus", () => document.querySelector('div.menu').style.display="unset")
}

document.querySelector("div.menu").addEventListener("blur", () => document.querySelector('div.menu').style.display="none")

document.querySelector("div.menu form").addEventListener("submit", () => document.querySelector('div.PokemonBar').insertAdjacentElement())
