import { router } from "./apiRoutes.js";
import { getUser } from "../services/getUser.js";
import { getReposUser } from "../services/getReposUser.js";


//rota para busca de nome de usuario
export function setUserRoute(){
  router.post("/buscar-usuario", async (req, res) => {
    const breadcrumbData = [
      { label: "Início", url: "/" },
      { label: "Usuário", url: "/buscar-usuario" },
    ];
  
    try {
      const { userName } = req.body;
      const user = await getUser(userName);
      const reposUser = await getReposUser(userName);
  
      res.render("user", { breadcrumbData, user, reposUser });
    } catch (error) {
      const err = "user";
      res.render("notFound", { breadcrumbData, err });
    }
});
}