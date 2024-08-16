// Importação do módulo 'activityService' que contém a função 'getFormattedActivity'
const { getFormattedActivity } = require("../Services/activityService");

// Definição da função assíncrona 'getActivity' que será exportada
const getActivity = async (req, res) => {
  try {
    // Chamada assíncrona à função 'getFormattedActivity' para obter uma atividade formatada
    const formattedActivity = await getFormattedActivity();

    // Registro no console da resposta obtida da API
    // console.log("Resposta da API:", formattedActivity);

    res.setHeader("Content-Type", "application/json"); // Define o cabeçalho da resposta como JSON
    res.writeHead(200); // Define o código de status da resposta como 200
    res.end(JSON.stringify(formattedActivity, null, 2)); // Envia a resposta com a piada formatada em formato JSON
  } catch (error) {
    // Caso ocorra um erro durante o processo acima, envia uma resposta de erro (código de status 500)
    // contendo uma mensagem genérica de erro e detalhes específicos do erro ocorrido
    res.status(500).json({ error: "Erro ao obter uma atividade" + error });
  }
};

// Exportação da função 'getActivity' para que possa ser utilizada em outros módulos
module.exports = {
  getActivity,
};
