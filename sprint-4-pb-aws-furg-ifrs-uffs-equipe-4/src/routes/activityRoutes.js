// Importação de módulos e funções necessários
const express = require("express"); // Importa o módulo Express, um framework web para Node.js
const { getActivity } = require("../Controllers/activityController"); // Importa a função getActivity do módulo activityController

// Cria um objeto Router do Express
const router = express.Router();

// Define uma rota HTTP GET para o caminho '/'
// Quando essa rota for acessada, a função getActivity do activityController será chamada
router.get("/", getActivity);

// Exporta o objeto Router para que ele possa ser utilizado em outros módulos
module.exports = router;
