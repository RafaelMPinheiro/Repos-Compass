const route = "https://rknjpqvs94.execute-api.us-east-1.amazonaws.com/";

document
  .getElementById("formDefault")
  .addEventListener("submit", function (event) {
    event.preventDefault();

    var radioSelected;
    var radios = document.getElementsByName("radioDefault");
    for (const radio of radios) {
      if (radio.checked) {
        radioSelected = radio.value;
        break;
      }
    }

    fetch(`${route}${radioSelected}`, {
      method: "GET",
    })
      .then((response) => response.text())
      .then((data) => {
        data = JSON.parse(data);
        document.getElementById("resultDefault").innerHTML = data.message;
      });
  });

document.getElementById("formTTS").addEventListener("submit", function (event) {
  event.preventDefault();

  var phrase = document.getElementById("phrase").value;
  var radioSelected;
  var radios = document.getElementsByName("radioTTS");
  for (const radio of radios) {
    if (radio.checked) {
      radioSelected = radio.value;
      break;
    }
  }

  if (radioSelected == undefined) {
    document.getElementById("resultDefault").innerHTML = "Selecione uma opção!";
    return;
  }

  fetch(`${route}${radioSelected}/tts`, {
    method: "POST",
    body: JSON.stringify({ phrase: phrase }),
    headers: {
      "Content-Type": "application/json",
      "Access-Control-Allow-Origin": "*",
    },
  })
    .then((response) => response.text())
    .then((data) => showResponse(JSON.parse(data)));
});

function showResponse(data) {
  document.getElementById("received_phrase").innerHTML = `Frase: "${data.received_phrase}"`;
  
  document.getElementById("url_to_audio").innerHTML = data.url_to_audio;
  document.getElementById("url_to_audio").href = data.url_to_audio;
  document.getElementById("linkResponse").style.display = "block"; 

  document.getElementById("created_audio").innerHTML = `Criado em: ${data.created_audio}`;

  if (data.unique_id) {
    document.getElementById("id_audio").innerHTML = `ID: ${data.unique_id}`;
  }

  document.getElementById("audio").src = data.url_to_audio;
  document.getElementById("audio").style.display = "block";
}