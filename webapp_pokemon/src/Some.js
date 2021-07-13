// function EventOnPokeball() {
//   let NumberBall = document.querySelector(".PokemonBar button").getAttribute('ClassName')
// }

for (let elem of document.querySelectorAll(".PokemonBar div button")){
  elem.addEventListener("focus", () => document.querySelector('div.menu').style.display="flex")
}

// let forma = document.querySelector('div.menu form');
// forma.addEventListener('submit', function(ev) {
//   if (document.querySelector("form input.PokemonID").value && (document.querySelector("form input.PokemonCP").value)) {
//     document.querySelector('.PokemonBar button').insertAdjacentHTML('afterbegin','<img src="/bibla" alt="">')
//     document.querySelector('.PokemonBar input').setAttribute(value,'document.querySelector("form input.PokemonCP").value')
//   }
// })
