const express = require('express');
const axios = require("axios");
const router = express.Router();
const dir = require('../public/dir')

//rota inicial
router.get("/", (req, res) => {
  res.sendFile(dir + "/index.html");
});

router.post("/buscar-repositorios", async (req, res) => {
  try {
    const { nomeRepositorio } = req.body;
    const response = await axios.get(
      `https://api.github.com/search/repositories?q=${nomeRepositorio}`
    );
    const repos = response.data.items.slice(0, 5).map((item) => ({
      nome: item.name,
      dono: item.owner.login,
      descricao: item.description,
      estrelas: item.stargazers_count,
      url: item.html_url,
    }));
    res.render("repos", { repos });
  } catch (error) {
    console.error(error);
    res.status(500).send("Erro ao buscar repositórios");
  }
});

router.post("/buscar-usuario", async (req, res) => {
  try {
    const { nomeUsuario } = req.body;
    const response = await axios.get(
      `https://api.github.com/users/${nomeUsuario}`
    
    );    
    const usuarioGit = response.data;
    let txtData = converteData(usuarioGit.created_at);
    const usuario= {
      avatar: usuarioGit.avatar_url, 
      nome: usuarioGit.name,
      login: usuarioGit.login,
      link: usuarioGit.html_url,
      dataCriacao: txtData,
      seguidores: usuarioGit.followers,
    } 
    res.render("usuario", { usuario })
  } catch (error) {
    console.error(error);
    res.status(500).send("Erro ao buscar usuário");
  }
})
function converteData (criadoEm){
  let data = new Date(criadoEm);
  let ano = data.getFullYear();
  let mes = data.getMonth() + 1;
  let dia = data.getDate();
  let txtData = dia + "/" + mes + "/" + ano;
  return txtData;
}
module.exports = router;