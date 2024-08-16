<h1 align="center"> Avaliação Sprint 4 - Equipe 4 </h1>

## API
Na realização da atividade proposta foi utilizadas as seguintes APIs:<br>
[Piadas](https://api.chucknorris.io/jokes/random)<br>
[Atividade](https://www.boredapi.com/api/activity)

## Tecnologias
 ![Node.JS](src/public/img/nodejs.png) ![GitHub](src/public/img/github.png) ![Axios](src/public/img/axios.png) ![AWS](src/public/img/aws.png)<br>
 
 ## Descrição 

Para a Sprint 4 foi proposta a busca de respostas em duas APIs, com a utilização de NodeJS, express e publicação através da AWS Cloud. <br>
Poderá ser realizado 3 tipos de consulta: Mensagem padrão (/), Piada (/api/piadas) e Atividade (/api/atividades).<br><br>
Ao realizar a busca por Mensagem padrão, será apresentada a seguinte mensagem:<br>
* "Este é o app do Grupo 4 😀"

Ao realizar a busca por Piada, seram apresentadas as seguintes informações: <br>

* Data de Atualizacao -> updated_at; <br>
* Data de Criação -> created_at;<br>
* Ícone -> icon_url;<br>
* Id -> id;<br>
* Piada -> value; <br>
* Referencia -> url;<br>

Ao realizar a busca por Piada, seram apresentadas as seguintes informações: <br>

* Id -> id;<br>
* Atividade -> activity; <br>
* Tipo -> type;<br>
* Participantes -> participants;<br>
* Acessibilidade -> accessibility; <br>

## Arquitetura
* ```src```
    * ```controllers```
        * ```activityController.js```
        * ```jokeController.js```
    * ```public```
        * ```img```    
   * ```routes```
        * ```activityRoute.js```
        * ```apiRoutes.js```
        * ```jokeRoute.js```
    * ```services```
        * ```getActivity.js```
        * ```getJoke.js```
    * ```app.js```

## Arquitetura AWS
![DiagramaAWS](https://github.com/FeMarzani/dio-desafio-github-primeiro-repositorio/assets/107329291/3a536b44-8b99-4fc8-9b02-8013505a8e30)


## Acessar Aplicação
Com o êxito da realização do Deploy na AWS Elastic Beanstalk, o acesso da aplicação, a partir das duas rotas da API e a raiz, pode-se dar da seguinte forma: <br>
1. Para o acesso inicial, com as informações da equipe, pode-se acessar através do seguinte link: **[Rota inicial](http://sprint4-projeto.us-east-1.elasticbeanstalk.com/)** <br>
```bash
http://sprint4-projeto.us-east-1.elasticbeanstalk.com/ 
```
2. Para o acesso a API de piadas, pode-se acessar através do seguinte link: **[API/Piadas](http://sprint4-projeto.us-east-1.elasticbeanstalk.com/api/joke)** <br>
```bash
http://sprint4-projeto.us-east-1.elasticbeanstalk.com/api/joke
```
3. Para o acesso a API de ativiades, pode-se acessar através do seguinte link: **[API/Atividades](http://sprint4-projeto.us-east-1.elasticbeanstalk.com/api/activity)** <br>
```bash
http://sprint4-projeto.us-east-1.elasticbeanstalk.com/api/activity
```

## Dificuldades Conhecidas
1. A principal dificuldade encontrada foi em relação ao deploy na Elastic Beanstalk. Entretanto, ao final da proposta de atividade a dificuldade foi sanada, o que possibilitou a conclusão do projeto.

## Integrantes

- 🔨 [Angemydelson Saint-Bert](https://github.com/angemydelson)
- 🔨 [Felipe Marzani](https://github.com/FeMarzani)
- 🔨 [Rafael Pinheiro](https://github.com/RafaMPinheiro)