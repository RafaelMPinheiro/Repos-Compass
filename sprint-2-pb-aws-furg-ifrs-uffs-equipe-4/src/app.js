const express = require("express");
const app = express();
const PORT = 3000;

app.set("view engine", "ejs");

app.use(express.urlencoded({ extended: true }));

app.use(express.static(__dirname + "/public"));

//rota inicial
app.get("/", (req, res) => {
  res.sendFile(dir +"/index.html");
});


app.use('/api', require('./routes/apiRoutes'));

//iniciar o express
app.listen(PORT, () => {
  console.log(`Servidor iniciado na porta ${PORT}`);
});
