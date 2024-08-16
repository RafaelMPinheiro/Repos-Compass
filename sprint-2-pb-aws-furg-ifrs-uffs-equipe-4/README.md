# Avaliação Sprint 2 - Equipe 4

## API
Para realização da atividade proposta optamos pela API do GitHub:<br>
[GitHub](https://docs.github.com/pt/rest?apiVersion=2022-11-28)

## Tecnologias
![HTML5](src/public/img/html5.png) ![CSS3](src/public/img/css3.png) ![BootSrap](src/public/img/bootstrap.png) ![Node.JS](src/public/img/nodejs.png) ![GitHub](src/public/img/github.png)

## Clone 
Para clonar a branch utilize o seguinte comando no terminal: <br> 
```git clone -b equipe-4 --single-branch https://github.com/Compass-pb-aws-2023-FURG-IFRS-UFFS/sprint-2-pb-aws-furg-ifrs-uffs.git``` 

## Descrição    
Foi proposto como atiividade da 2ª Sprint o desenvolvimento de um software que busca consumir uma [API](https://any-api.com), utilizando Node.js e as funções que a API disponibiliza. <br>
Poderá ser realizado dois tipos de consulta: Reposítório e Usuário.<br><br>
Ao realizar a busca por Repositório, serão apresentadas as seguintes informações:<br>
* Nome do Repositório;<br>
* Dono do Reposítório;<br>
* Descrição do Repositório;<br>
* Avaliação do Repositório.<br>
* URL;

Ao realizar a busca por Usuário, seram apresentadas as seguintes informações: <br>

* Avatar; <br>
* Usuário;<br>
* Link para o GitHub do usuário;<br>
* Nome do usuário;<br>
* Data de criação do perfil; <br>
* Quantidade de seguidores.<br>

## Arquitetura
* ```src```
    * ```public```
        * ```css```
            * ```index.css```
            * ```repos.css```
            * ```styles.css```
            * ```usuaro.css```
        * ```img```
        * ```dir.js```
        * ```index.html```
    * ```routes```
        * ```aiRoues.css```
    * ```views```
        * ```repos.ejs```
        * ```usuario.ejs```
    * ```app.js```

## Acessar Aplicação
* Realizar o clone do Repositório: <br>
```git clone -b equipe-4 --single-branch https://github.com/Compass-pb-aws-2023-FURG-IFRS-UFFS/sprint-2-pb-aws-furg-ifrs-uffs.git``` <br>
* Instalar dependências: <br>
```npm install```<br>
* Abrir o arquivo ```app.js``` no terminal e executar o comando:<br>
```npm run dev```<br>
* Abrir o navegador e acessar:<br>
```localhost:3000``` <br>

## Utilização 
* Na página inicial há duas opções de pesquisa:
    * Repositório
    * Usuário
* Escolha um dos campos e preencha conforme o indicado;<br>
* Clique no botão "buscar", abaixo do campo selecionado;<br>
* A aplicação irá realizar a consulta solicitada pelo usuário:
    * Em caso de escolha de buscar por repositórios, serão exibidos 5 reposiórios que possuam o nome informado na busca;
    * Em caso de escolha por busca usuário, serão exibidas as inforações relativas ao usuário correspondente. 

## Dificuldades Conhecidas
1- Por se tratar da primeira atividade em grupo, tivemos dificuldade para organizar e dividir as tarefas a serem desempenhadas por cada membro, portanto, algumas vezes trechos de código foram realizados em duplas.

## Integrantes

- 🔨 Fabiano Mendonça
- 🔨 John Marcel Silveira
- 🔨 Rafael Pinheiro
- 🔨 Yuri Souza

| [<img src="https://avatars.githubusercontent.com/u/54964022?v=4" width=85><br><sub>Fabiano Mendonça</sub>](https://github.com/FabianoMendonca) | [<img src="https://avatars.githubusercontent.com/u/29494433?v=4" width=85><br><sub>John Marcel Silveira</sub>](https://github.com/JohnMarcelSilveira) | [<img src="https://avatars.githubusercontent.com/u/49412094?v=4" width=85><br><sub>Rafael Pinheiro</sub>](https://github.com/RafaMPinheiro) | [<img src="https://avatars.githubusercontent.com/u/30680769?v=4" width=85><br><sub>Yuri Souza</sub>](https://github.com/Zeeneboch) |
| :--------------------------------------------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------------------------------------: | ---------------------------------------------------------------------------------------------------------------------------------- |
