const num = 123;

var button = document.querySelector("#button");
var input = document.getElementById("input");
var dica = document.getElementById("dica");

button.addEventListener("click", () => {
  dica.innerHTML = handleSubmit(input.value);
  if (input.value == num) {
    dica.style.color = "green";
  } else {
    dica.style.color = "red";
  }
});

const handleSubmit = (tentativa) => {
  if (tentativa == num) return "Parabéns você acertou!";

  if (tentativa > num) {
    if (tentativa > 1.5 * num) {
      return "Tentativa foi muito maior!";
    } else {
      return "Tentativa foi maior!";
    }
  } else if (tentativa < num) {
    if (tentativa < 0.5 * num) {
      return "Tentativa foi muito menor!";
    } else {
      return "Tentativa foi menor!";
    }
  }
};
