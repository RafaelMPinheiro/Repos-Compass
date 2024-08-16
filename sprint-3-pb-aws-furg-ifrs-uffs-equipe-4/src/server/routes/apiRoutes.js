import express from "express";
import { dir } from "../../public/dir.js";
import { setRepositoryRoute } from "./repositoryRoute.js";
import { setUserRoute } from "./userRoute.js";

const router = express.Router();

//rota inicial
router.get("/", (req, res) => {
  res.sendFile(dir + "/index.html");
});

setRepositoryRoute();

setUserRoute();

export {router} ;
