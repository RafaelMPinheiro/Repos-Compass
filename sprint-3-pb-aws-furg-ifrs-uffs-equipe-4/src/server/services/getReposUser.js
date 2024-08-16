import axios from "axios";

export async function getReposUser(userName) {
  const response = await axios.get(
    `https://api.github.com/users/${userName}/repos`
  );
  const repos = response.data.slice(0, 5).map((item) => ({
    name: item.name,
    owner: item.owner.login,
    description: item.description ? item.description : "Sem descrição",
    stars: item.stargazers_count,
    url: item.html_url,
  }));

  return repos;
}
