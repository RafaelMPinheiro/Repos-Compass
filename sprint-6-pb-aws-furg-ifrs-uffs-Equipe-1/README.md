<div align="center">
  <img src="src/assets/logo.png" alt="Logo UOL" width="120px" height="120px">

</div>

<div align="center">
  <h1>UOLvoice</h1>
  <h2>Conversor de texto para áudio</h2>
</div>

## 🚀 Descrição

O propósito central deste projeto era criar uma página HTML que irá capturar uma frase qualquer inserida pelo usuário e transformará essa frase em um audio em mp3 via polly. Em 3 passos:

1. Processar o texto enviado pelo usuário, transformá-lo em um arquivo de áudio no formato .MP3 e guardar esse áudio no serviço de armazenamento S3 da AWS. Por fim, fornecer ao usuário um link para baixar o áudio que foi criado.

2. Processar o texto fornecido pelo usuário, convertê-lo em um arquivo de áudio .MP3 e salvar esse áudio no serviço de armazenamento S3 da AWS. Além disso, registrar as informações do arquivo .MP3 em um banco de dados DynamoDB e disponibilizar ao usuário um link para fazer o download do áudio produzido.

3. Analisar o texto recebido do usuário, verificar se ele já existe ou não na base de dados do aplicativo. Se ainda não estiver presente, transformá-lo em um arquivo de áudio .MP3, armazená-lo no DynamoDB e entregar ao usuário um link para baixar o áudio gerado.

## 📺 Preview
![preview](https://github.com/FeMarzani/dio-desafio-github-primeiro-repositorio/assets/107329291/26361189-72ef-4faa-acaf-d7d27769bae8)

Link: [https://uolvoice.d4oqb1k2br7pi.amplifyapp.com/](https://uolvoice.d4oqb1k2br7pi.amplifyapp.com)

## 🔧 Instalação

1. Clone o repositório e entre na branch Equipe-1.

```bash
git clone https://github.com/Compass-pb-aws-2023-FURG-IFRS-UFFS/sprint-6-pb-aws-furg-ifrs-uffs.git
git checkout Equipe-1
```

2. Instale o framework serverless em seu computador. Mais informações [aqui](https://www.serverless.com/framework/docs/getting-started)

```bash
npm install -g serverless
```

3. Gere suas credenciais (AWS Acess Key e AWS Secret) na console AWS pelo IAM. Mais informações [aqui](https://www.serverless.com/framework/docs/providers/aws/guide/credentials/)

4. Em seguida insira as credenciais e execute o comando conforme exemplo:

```bash
serverless config credentials \
  --provider aws \
  --key AKIAIOSFODNN7EXAMPLE \
  --secret wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
```

Também é possivel configurar via [aws-cli](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) executando o comando:

```bash
$ aws configure
AWS Access Key ID [None]: AKIAIOSFODNN7EXAMPLE
AWS Secret Access Key [None]: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
Default region name [None]: us-east-1
Default output format [None]: ENTER
```

## 📦 Implantação

1. Para efetuar o deploy da solução na sua conta aws execute (acesse a pasta `api-tts`):

```bash
serverless deploy
```

2. Alternativamente, também é possível emular API Gateway e Lambda localmente usando serverless-offlineplugin. Para fazer isso, execute o seguinte comando:

```bash
serverless plugin install -n serverless-offline
```

Após a instalação, você pode iniciar a emulação local com:

```
serverless offline
```

## ⚙️ Executando os testes

### Rota 1 → Get /

- Resposta a ser entregue:

```json
  {
    "message": "Go Serverless v3.0! Your function executed successfully!",
    "input": {
        ...(event)
      }
  }
```

### Rota 2 → Get /v1

- Resposta a ser entregue:

```json
{
  "message": "TTS api version 1."
}
```

### Rota 3 → Get /v2

- Resposta a ser entregue:

```json
{
  "message": "TTS api version 2."
}
```

### Rota 4 -> Post /v1/tts

- Entrada teste:

```json
{
  "phrase": "converta esse texto para áudio"
}
```

- Resposta a ser entregue:

```json
{
  "received_phrase": "converta esse texto para áudio",
  "url_to_audio": "https://meu-buckect/audio-xyz.mp3",
  "created_audio": "02-02-2023 17:00:00"
}
```

### Rota 5 -> Post /v2/tts

- Entrada teste:

```json
{
  "phrase": "converta esse texto para áudio e salve uma referencia no dynamoDB"
}
```

- Resposta a ser entregue:

```json
{
  "received_phrase": "converta esse texto para áudio",
  "url_to_audio": "https://meu-buckect/audio-xyz.mp3",
  "created_audio": "02-02-2023 17:00:00",
  "unique_id": "123456"
}
```

### Rota 6 -> Post /v3/tts

- Entrada teste:

```json
{
  "phrase": "converta esse texto para áudio e salve uma referencia no dynamoDB. Caso a referencia já exista me devolva a URL com audio já gerado"
}
```

- Resposta a ser entregue:

```json
{
  "received_phrase": "converta esse texto para áudio",
  "url_to_audio": "https://meu-buckect/audio-xyz.mp3",
  "created_audio": "02-02-2023 17:00:00",
  "unique_id": "123456"
}
```

## 🛠️ Construído com

- [API Gateway](https://aws.amazon.com/pt/api-gateway/) - Serviço de gerenciamento das rotas da API
- [Lambda](https://aws.amazon.com/pt/lambda/) - Faz a conexão dos códigos entre a WEB e a Nuvem (AWS)
- [Amazon Polly](https://aws.amazon.com/pt/polly/) - Tecnologia para sintetizar textos em fala
- [S3](https://aws.amazon.com/pt/s3/) - Armazenamento dos áudios gerados
- [DynamoDB](https://aws.amazon.com/pt/dynamodb/) - Sistema de armazenamento estruturado para a localização de áudios já gerados

<img src="./assets/arquitetura.png"/>

## 💪​ Dificuldades encontradas

* Divisão de responsabilidades entre as funções
* Configuração da Polly para melhor leituras

## ✒️ Autores

- [**Denner Gutierres**](https://github.com/dennerguti)
- [**Felipe Marzani**](https://github.com/FeMarzani)
- [**Marcone de Freitas**](https://github.com/Marcone-Sudo)
- [**Rafael Pinheiro**](https://github.com/RafaMPinheiro)
