// Importação do módulo 'jokeService' que contém a função 'getFormattedJoke'
const { getFormattedJoke } = require("../Services/jokeService");

// Definição da função assíncrona 'getJoke' que será exportada
const getJoke = async (req, res) => {
  try {
    // Chamada assíncrona à função 'getFormattedJoke' para obter uma piada formatada
    const formattedJoke = await getFormattedJoke();

    // Registro no console da resposta obtida da API de piadas
    // console.log("Resposta da API:", formattedJoke);

    res.setHeader("Content-Type", "application/json"); // Define o cabeçalho da resposta como JSON
    res.writeHead(200); // Define o código de status da resposta como 200
    res.end(JSON.stringify(formattedJoke, null, 2)); // Envia a resposta com a piada formatada em formato JSON
  } catch (error) {
    // Caso ocorra um erro durante o processo acima, envia uma resposta de erro (código de status 500)
    // contendo uma mensagem genérica de erro, indicando uma falha ao obter a piada
    res.status(500).json({ error: "Erro ao obter piada" });
  }
};

// Exportação da função 'getJoke' para que possa ser utilizada em outros módulos
module.exports = {
  getJoke,
};
