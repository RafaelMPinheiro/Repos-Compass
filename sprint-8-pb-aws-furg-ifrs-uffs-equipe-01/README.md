# <p align="center"> <text>IDENTIFIER</text>

## <p align="center"> Tecnologias Utilizadas

<p align="center">
<img src="assets\icons\python.png">
<img src="assets\icons\aws.png">
<img src="assets\icons\rekognition.png">
<img src="assets\icons\cloudwatch.png">
<img src="assets\icons\lambda.png">
<img src="assets\icons\s3.png">
</p>

## <p align="center"> Integrantes
<p align="center">
<a href="https://www.linkedin.com/in/fabiano-mendon%C3%A7a-40435a202/"> <img src="https://img.shields.io/badge/Fabiano Mendonça-0077B5?style=for-the-badge&logo=linkedin&logoColor=white">
<a href="https://www.linkedin.com/in/paulo-sergio-nunes-48750316b/"> <img src="https://img.shields.io/badge/Paulo Sergio Nunes-0077B5?style=for-the-badge&logo=linkedin&logoColor=white">
<a href="https://www.linkedin.com/in/rafamessiaspinheiro/"> <img src="https://img.shields.io/badge/Rafael Pinheiro-0077B5?style=for-the-badge&logo=linkedin&logoColor=white">
<a href="https://www.linkedin.com/in/yuri-antunes-souza/"> <img src="https://img.shields.io/badge/Yuri Antunes Souza-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"></a>

## <p align="center"> Objetivo

<p> Com base nos estudos de Visão Computacional e AWS Rekognition, foi desenvolvido um serviço com intuito de identificar os labels que compõem uma imagem.

## Utilização
* Para utilizar as rotas apresentadas neste documento basta possuir o postman, ou similar, instalado no seu computador. <br>

### POST /v1/vision

<p> Preencha o campo response do Postman com o seguinte formato: <br>

```json 
{
    "bucket": "tf-s3-sp8",
    "imageName": "a3.jpg"
}
```
- ```Bucket``` é o nome do S3 instanciado na AWS; <br>
- ```imageName``` é o nome da imagem salva no bucket.<br>

<p> No campo response será retornado um JSON conforme abaixo: <br>

```json
{
    "url_to_image": "https://tf-s3-sp8.s3.amazonaws.com/a3.jpg",
    "created_image": "27-09-2023 02:23:19",
    "labels": [
        {
            "Confidence": 99.99866485595703,
            "Name": "Animal"
        },
        {
            "Confidence": 99.99866485595703,
            "Name": "Canine"
        },
        {
            "Confidence": 99.99866485595703,
            "Name": "Dog"
        },
        {
            "Confidence": 99.99866485595703,
            "Name": "Golden Retriever"
        },
        {
            "Confidence": 99.99866485595703,
            "Name": "Mammal"
        },
        {
            "Confidence": 99.99866485595703,
            "Name": "Pet"
        }
    ]
}
``` 
### POST /v2/vision

<p> Preencha o campo response do Postman com o seguinte formato: <br>

```json 
{
    "bucket": "tf-s3-sp8",
    "imageName": "a3.jpg"
}

```
- ```Bucket``` é o nome do S3 instanciado na AWS; <br>
- ```imageName``` é o nome da imagem salva no bucket.<br>

<p> No campo response será retornado um JSON conforme abaixo, podendo variar se a imagem conter 2 ou mais faces: <br>

```json
{
    "url_to_image": "https://tf-s3-sp8.s3.amazonaws.com/u9.jpg",
    "created_image": "02-10-2023 02:02:42",
    "faces": [
        {
            "position": {
                "Height": 0.6598449945449829,
                "Left": 0.5789735913276672,
                "Top": 0.019625544548034668,
                "Width": 0.3684956431388855
            },
            "classified_emotion": "SAD",
            "classified_emotion_confidence": 99.99140167236328
        }
    ]
}
```

- Caso a imagem passada não contenha faces será retornado o seguinte objeto JSON: <br>

```json
{
    "url_to_image": "https://tf-s3-sp8.s3.amazonaws.com/a1.jpg",
    "created_image": "02-10-2023 02:02:41",
    "faces": [
        {
            "position": {
                "Height": null,
                "Left": null,
                "Top": null,
                "Width": null
            },
            "classified_emotion": null,
            "classified_emotion_confidence": null
        }
    ]
}

```
## <p align="center"> Deploy do Projeto
### Terraform
<p> Utilizou-se a ferramenta Terraform para instanciar a arquitetura utilizada pela aplicação na AWS.
<p> A arquitetura resume-se a um S3, para armazenar as imagens que serão analisadas pela aplicação, sendo que o upload das imagens também foi realizado via Terraform. 
 
### Serverless
<p> O projeto foi colocado em produção através do Framework Serverless. 

## Reprodução do Projeto

* Clone o repositório através do comando abaixo:<br>
```git clone -b equipe-01 https://github.com/Compass-pb-aws-2023-FURG-IFRS-UFFS/sprint-8-pb-aws-furg-ifrs-uffs.git ```
<br>

* Após realizado o clone, preencha o arquivo ```terraform.tfvars```;
* Abra o projeto através do terminal, abra a pasta terraform e execute os seguintes comandos: 
- ```terraform init```
- ```terraform plan```
- ```terraform apply```

* Acesse a pasta "visão-computacional" através do terminal e execute o comando serverless: 
```serverless deploy```

* Ao término da execução do serverless serão retornados os endpoints das rotas.

## Rotas
Foram implementadas as seguintes rotas no projeto: 

* GET <br>
```https://p8e0jd1450.execute-api.us-east-1.amazonaws.com/```

* GET /v1 <br>
```https://p8e0jd1450.execute-api.us-east-1.amazonaws.com/v1```

* GET /v2 <br>
```https://p8e0jd1450.execute-api.us-east-1.amazonaws.com/v2```

* POST /v1/vision <br>
```https://p8e0jd1450.execute-api.us-east-1.amazonaws.com/v1/vision```

* POST /v2/vision <br>
```https://p8e0jd1450.execute-api.us-east-1.amazonaws.com/v2/vision```

## Arquitetura do Projeto

### Arquitetura AWS
<p align="center">
<img src="assets\icons\arquiteturaaws.png">
</p>

### Arquitetura de pastas
* .vscode
* assets
  * icons
  * ImageDataset
* terraform
  * main.tf
  * terraform.tfvars
  * variables.tf
* visão-computacional
  * serverless
  * routes 
    * v1
      * v1_description.py
      * v1_vision.py
    * v2
      * v2_description.py
      * v2_vision.py
    * health.py
  * util
    * detect_faces.py
    * detect_labels.py
    * get_date.py
  * package.json
  * serverless.yml 

## Dificuldades Encontradas
* A maior dificuldade enfrentada na atividade foi criar a instância do S3, de forma pública e com as imagens, através do terraform. Entretando consultando a documentação e fóruns o problema foi solucionado. <br>


