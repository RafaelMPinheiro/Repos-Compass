// Importações de módulos e funções necessários
const { v4: uuidv4 } = require("uuid"); // Importa a função v4 da biblioteca uuid para gerar IDs únicos
const axios = require("axios"); // Importa o módulo Axios para fazer requisições HTTP

// Carregando as variáveis de ambiente do .env
const path = require("path");
require("dotenv").config({ path: path.join(__dirname, "../config/.env") }); 

// Definição da função assíncrona 'getFormattedJoke' que será exportada
const getFormattedJoke = async () => {
  try {

    const API_JOKE = process.env.API_JOKE;
    // Faz uma requisição GET para a API de piadas do Chuck Norris
    const response = await axios.get(API_JOKE);
    const joke = response.data; // Armazena os dados da piada da resposta

    // Formata os dados da piada em um novo objeto
    const formattedJoke = {
      updated_at: formatDate(joke.updated_at), // Data de atualização formatada
      created_at: formatDate(joke.created_at), // Data de criação formatada
      icon_url: joke.icon_url, // URL do ícone da piada
      id: uuidv4(), // Gera um ID único usando a função uuidv4
      value: joke.value.replace(/Chuck Norris/g, "CHUCK NORRIS"), // Texto da piada com "Chuck Norris" substituído por "CHUCK NORRIS"
      url: joke.url, // URL de referência para a piada
    };

    // Retorna o objeto formatado
    return formattedJoke;
  } catch (error) {
    // Caso ocorra um erro durante o processo, lança uma exceção com uma mensagem de erro
    throw new Error("Erro ao obter piada");
  }
};

// Função para formatar uma data no formato "dd/mm/yyyy"
const formatDate = (dateString) => {
  const date = new Date(dateString);
  const day = String(date.getDate()).padStart(2, "0");
  const month = String(date.getMonth() + 1).padStart(2, "0");
  const year = date.getFullYear();
  return `${day}/${month}/${year}`;
};

// Exporta a função 'getFormattedJoke' para que possa ser utilizada em outros módulos
module.exports = {
  getFormattedJoke,
};
