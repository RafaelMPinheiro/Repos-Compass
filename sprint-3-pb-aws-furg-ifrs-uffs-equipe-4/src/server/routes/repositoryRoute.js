import { router } from "./apiRoutes.js";
import { getRepo } from "../services/getRepo.js";


//rota para busca de repositorios
export function setRepositoryRoute (){
  router.post("/buscar-repositorios", async (req, res) => {
    const breadcrumbData = [
      { label: "Início", url: "/" },
      { label: "Repositórios", url: "/buscar-repositorios" },
    ];
  
    try {
      const { repositoryName } = req.body;
      const repos = await getRepo(repositoryName);
  
      res.render("repos", { breadcrumbData, repos });
    } catch (error) {
      const err = "repository";
      res.render("notFound", { breadcrumbData, err });
    }
  });
}
