import axios from "axios";

export async function getUser(userName) {
  const response = await axios.get(`https://api.github.com/users/${userName}`);

  const userGit = response.data;
  let formattedDate = convertDate(userGit.created_at);
  const user = {
    avatar: userGit.avatar_url,
    name: userGit.name,
    login: userGit.login,
    link: userGit.html_url,
    created_at: formattedDate,
    followers: userGit.followers,
  };

  return user;
}

function convertDate(created_at) {
  let date = new Date(created_at);
  let year = date.getFullYear().toString();
  let month = (date.getMonth() + 1).toString().padStart(2, "0");
  let day = date.getDate().toString().padStart(2, "0");
  let formattedDate = day + "/" + month + "/" + year;
  return formattedDate;
}
