// function EventOnPokeball() {
//   let NumberBall = document.querySelector(".PokemonBar button").getAttribute('ClassName')
// }

for (let elem of document.querySelectorAll(".Hero .PokemonBar div button")){
  elem.addEventListener("focus", () => document.querySelector('.Hero div.menu').style.display="flex")
}
for (let elem of document.querySelectorAll(".Opponent .PokemonBar  div button")){
    elem.addEventListener("focus", () => document.querySelector('.Opponent div.menu').style.display="flex")
}

// let forma = document.querySelector('div.menu form');
// forma.addEventListener('submit', function(ev) {
//   if (document.querySelector("form input.PokemonID").value && (document.querySelector("form input.PokemonCP").value)) {
//     document.querySelector('.PokemonBar button').insertAdjacentHTML('afterbegin','<img src="/bibla" alt="">')
//     document.querySelector('.PokemonBar () input').setAttribute(value,'document.querySelector("form input.PokemonCP").value')
//     document.querySelector('.PokemonBar (регулярное выражение, которое должно указывать конкретный номер мяча) input').setAttribute(visability,'visible')
//   }
// })

let searchWord = ""
let buvisan = document.querySelector(".PokemonID")
buvisan.addEventListener("focus", () => searchWord = buvisan.value.toString())
buvisan.addEventListener("input",() => searchWord = buvisan.value.toString())

async function SendPost(){
  let response = await fetch('http://localhost:8000/api', {
     method: 'POST',
     headers: {
       'Content-Type': 'application/json',
       'Accept': 'application/json'},
     mode:"cors",
     body: JSON.stringify({query:"{ hello }"})
  });
  let data = await response.json();
  console.log(data.data)
}

let X = document.querySelector(".menu .X")
X.addEventListener("click", SendPost)