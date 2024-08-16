import express from "express";
import {dir} from '../public/dir.js';
import { router } from "./routes/apiRoutes.js";

const server = express();
const PORT = 3000;


server.set("view engine", "ejs");

server.use(express.urlencoded({ extended: true }));

server.use(express.static("./public"));

//rota inicial
server.get("/", (req, res) => {
  res.sendFile( dir +"/index.html");
});


server.use('/api', router);

//iniciar o express
export function startServer(){
  server.listen(PORT, () => {
    console.log(`Servidor iniciado na porta ${PORT}`);
  });  
} 

