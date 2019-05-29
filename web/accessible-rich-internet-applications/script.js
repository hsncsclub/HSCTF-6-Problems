var template = (bit, a, b) => `
<div role="option" aria-posinset="${a}" aria-setsize="${b}">${bit}</div>
`
String.prototype.leftJustify = function( length, char ) {
    var fill = [];
    while ( fill.length + this.length < length ) {
      fill[fill.length] = char;
    }
    return fill.join('') + this;
}
var toBits = str => str.split("").map(a => a.charCodeAt(0).toString(2).leftJustify (8, "0")).join("");

var encoded = toBits("im gonna add some filler text here so the page is a bit longer. lorem ipsum... here's the flag btw, flag{accessibility_is_crucial}")
var parts = encoded.split("").map((bit,i) => template(bit, i,encoded.length));

function shuffle(array) {
  var currentIndex = array.length, temporaryValue, randomIndex;

  // While there remain elements to shuffle...
  while (0 !== currentIndex) {

    // Pick a remaining element...
    randomIndex = Math.floor(Math.random() * currentIndex);
    currentIndex -= 1;

    // And swap it with the current element.
    temporaryValue = array[currentIndex];
    array[currentIndex] = array[randomIndex];
    array[randomIndex] = temporaryValue;
  }

  return array;
}

console.log(shuffle(parts).join(""))