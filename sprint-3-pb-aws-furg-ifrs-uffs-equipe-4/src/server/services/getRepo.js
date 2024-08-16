import axios from "axios";

export async function getRepo(repoName) {
  const response = await axios.get(
    `https://api.github.com/search/repositories?q=${repoName}`
  )
  const repos = response.data.items.slice(0, 5).map((item) => ({
    name: item.name,
    owner: item.owner.login,
    description: item.description,
    stars: item.stargazers_count,
    url: item.html_url,
  }));
  
  return repos;
}