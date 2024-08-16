<h1 align="center"> Reserva Model - Equipe 2 </h1>


## Descrição do Projeto
<p style="text-align:justify;">O propósito central deste projeto era criar um modelo treinado por meio do SageMaker, o qual permitiria a realização de consultas por meio de uma API que inclui uma rota dedicada a esse fim. O processo de treinamento do modelo no SageMaker envolveu a utilização do seguinte conjunto de dados <a href="https://www.kaggle.com/datasets/ahsan81/hotel-reservations-classification-dataset">dataset</a>. A fim de efetuar consultas, é empregada uma requisição do tipo POST.</p>

## Integrantes


| Nome                 | Linkedin                                                            |
| -------------------- | ------------------------------------------------------------------- |
| John Marcel Silveira | [Link](https://www.linkedin.com/in/john-marcel-silveira-62530752/)  |
| Rafael Pinheiro      | [Link](https://www.linkedin.com/in/rafamessiaspinheiro/)            |
| Josué Fernandes      | [Link](https://www.linkedin.com/in/josu%C3%A9-mendon%C3%A7a-dev77/) |
</div>


## Aplicação

- [Reserva Model](http://sprint5-equipe2.us-east-1.elasticbeanstalk.com/)
## Tecnologias Utilizadas


<div style="display:flex;center;gap:5px">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original-wordmark.svg" width="40"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/amazonwebservices/amazonwebservices-plain-wordmark.svg"  width="40"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/flask/flask-original.svg" width="40" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original-wordmark.svg" width="40" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/jupyter/jupyter-original.svg" width="40"/>        
</div>


<div style="display:flex;justify-content: center;flex-direction:column">


## Rotas

### Rota → Get /

1. Nesta rota será efetuado um get na raiz do projeto.

```json
 Este é o app do Grupo 2 😀
```

2. Status code para sucesso da requisição será `200`

***
### Rota → Post /api/v1/predict

1. Nesta rota será efetuado um post no formato
```json
{
  "no_of_adults": 2,
  "no_of_children": 0,
  "no_of_weekend_nights": 1,
  "no_of_week_nights": 2,
  "type_of_meal_plan": "Meal Plan 3",    
  "required_car_parking_space": 0,
  "room_type_reserved": "Room_Type 4",
  "lead_time": 224,
  "arrival_year": 2023,
  "arrival_month": 10,
  "arrival_date": 2,
  "market_segment_type":"Offline",
  "repeated_guest": 0,
  "no_of_special_requests": 0
} 
```

2. O retorno da API a ser desenvolvida deverá estar na seguinte formatação:

```json
{
  "result" 0
}
```
## Arquitetura Aws

![Diagrama sprint5-equipe2](https://github.com/Compass-pb-aws-2023-FURG-IFRS-UFFS/sprint-5-pb-aws-furg-ifrs-uffs/assets/99553096/64885da9-214f-4c0c-b101-703ae72fa4f8)


## Estrutura de Pastas do projeto:

- **src**
  - **controllers**
    - ```previsaoController.py```
  - **models**
    - ```previsaoModel.py```
    - ```reservaModel.py```
  - **routes**
    - **api_v1**
      - **endpoints**
        - ```predict.py```
    - ```home.py```
  - **services**
    - ```previsaoService.py```
  - **utils**
    - `helper.py`
  - `.example.env`
  - `dockerfile`
  - `main.py`
  - `requirements.txt`
- **notebook**
  - `Hotel_Reservations.csv`
  - `sprint5-final.ipynb`
- `Diagrama sprint5-equipe2.png`
- `README.md`
## Licença
Internet Systems Consortium license

Copyright (c) 2023, Equipe-3

É concedida permissão para usar, copiar, modificar e/ou distribuir este software para qualquer finalidade, com ou sem taxa, desde que o aviso de direitos autorais acima e este aviso de permissão apareçam em todas as cópias.
