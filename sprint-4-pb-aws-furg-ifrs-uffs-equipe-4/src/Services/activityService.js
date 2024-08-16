// Importações de módulos e funções necessários
const { v4: uuidv4 } = require("uuid"); // Importa a função v4 da biblioteca uuid para gerar IDs únicos
const axios = require("axios"); // Importa o módulo Axios para fazer requisições HTTP

// Carregando as variáveis de ambiente do .env
const path = require("path");
require("dotenv").config({ path: path.join(__dirname, "../config/.env") }); 

// Definição da função assíncrona 'getFormattedActivity' que será exportada
const getFormattedActivity = async () => {

  const API_ATT = process.env.API_ATT
  // Faz uma requisição GET para a API de atividades
  const response = await axios.get(API_ATT);
  const activity = response.data; // Armazena os dados da atividade da resposta

  // Formata os dados da atividade em um novo objeto
  const formattedActivity = {
    id: uuidv4(), // Gera um ID único usando a função uuidv4
    activity: activity.activity, // Nome da atividade
    type: activity.type, // Tipo da atividade
    participants: activity.participants, // Número de participantes
    accessibility: (activity.accessibility * 100) + "%", // Acessibilidade formatada em porcentagem
  };

  // Retorna o objeto formatado
  return formattedActivity;
};

// Exporta a função 'getFormattedActivity' para que possa ser utilizada em outros módulos
module.exports = {
  getFormattedActivity,
};
