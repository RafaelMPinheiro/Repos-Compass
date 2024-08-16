const express = require("express");
const activityRoutes = require("./routes/activityRoutes");
const jokeRoutes = require("./routes/jokeRoutes");

require('dotenv').config()
const PORT = process.env.PORT || 8080;

const app = express();

app.use(express.json());

// Rota de saúde
app.get("/health", (req, res) => {
  res.status(200).json({ status: "Server is healthy" });
});

// Rotas de API
app.use("/api/activity", activityRoutes);
app.use("/api/joke", jokeRoutes);

// Rota padrão
app.get("/", (req, res) => {
  res.send("Este é o app do Grupo 4 😀").status(200);
});

// Tratamento de erro para rotas não encontradas
app.use((req, res) => {
  res.status(404).json({ error: "Rota não encontrada" });
});

// Middleware de tratamento de erros
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({ error: "Erro interno do servidor" });
});

app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}.`);
});
