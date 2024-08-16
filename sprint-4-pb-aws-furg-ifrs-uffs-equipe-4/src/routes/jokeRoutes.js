// Importação de módulos e funções necessários
const express = require("express"); // Importa o módulo Express, um framework web para Node.js
const { getJoke } = require("../Controllers/jokeController"); // Importa a função getJoke do módulo jokeController

// Cria um objeto Router do Express
const router = express.Router();

// Define uma rota HTTP GET para o caminho '/'
// Quando essa rota for acessada, a função getJoke do jokeController será chamada
router.get("/", getJoke);

// Exporta o objeto Router para que ele possa ser utilizado em outros módulos
module.exports = router;
