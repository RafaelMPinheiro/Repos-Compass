# 🚀 Repos-Compass: Jornada Prática em AWS (FURG, IFRS, UFFS)

## ✨ Sobre o Projeto

**Repos-Compass** reúne as entregas que fiz no Programa de Bolsas da Compass UOL, no curso de **Práticas de AWS (PB-AWS)**, uma parceria entre FURG, IFRS e UFFS. Cada pasta `sprint-X...` guarda o código e o README de uma sprint. A Sprint 1 foi individual; da 2 à 9-10 o trabalho foi em equipe, e a equipe aparece no nome da pasta.

Os READMEs de cada sprint são a fonte das informações abaixo. Para detalhes, rotas e instruções de execução, abra o `README.md` da pasta.

## 🛠️ Tecnologias Utilizadas

Pelo que os READMEs das sprints descrevem:

*   **Linguagens e front-end:** JavaScript, Node.js (Express), Python, HTML, CSS e Bootstrap.
*   **Contêineres:** Docker e Docker Compose, com a imagem publicada no Docker Hub e executada numa instância EC2.
*   **Hospedagem e deploy:** AWS Elastic Beanstalk, AWS Amplify, Serverless Framework e Terraform.
*   **Serverless e dados:** AWS Lambda, Amazon S3 e Amazon DynamoDB.
*   **IA e linguagem:** Amazon SageMaker (modelo de reservas), Amazon Polly, Amazon Lex, Amazon Rekognition e Amazon Transcribe.
*   **Integrações:** Slack, WhatsApp via Twilio e a API do GitHub.

## 📂 Estrutura de Sprints

*   **sprint-1-pb-aws-furg-ifrs-uffs-rafael-pinheiro:** sistema de verificação de PIN em JavaScript. O usuário informa um número e recebe a dica de que o próximo valor deve ser maior, muito maior, menor ou muito menor.
*   **sprint-2-pb-aws-furg-ifrs-uffs-equipe-4:** aplicação Node.js que consome a API do GitHub e consulta repositórios e usuários.
*   **sprint-3-pb-aws-furg-ifrs-uffs-equipe-4:** a aplicação da Sprint 2 em contêiner Docker, com docker-compose, e publicada numa instância EC2.
*   **sprint-4-pb-aws-furg-ifrs-uffs-equipe-4:** API em Node.js e Express que consulta duas APIs públicas (piadas e atividades), com deploy no AWS Elastic Beanstalk.
*   **sprint-5-pb-aws-furg-ifrs-uffs-equipe-2:** modelo de previsão de reservas treinado no SageMaker, com uma API que o consulta (rota `POST /api/v1/predict`), publicada no Elastic Beanstalk.
*   **sprint-6-pb-aws-furg-ifrs-uffs-Equipe-1:** UOLvoice, que converte texto em áudio MP3 com o Amazon Polly, guarda o arquivo no S3 e registra os dados no DynamoDB. O deploy usa o Serverless Framework, e a página fica no Amplify.
*   **sprint-7-pb-aws-furg-ifrs-uffs-equipe-2:** UOL Bank, um chatbot bancário feito com o Amazon Lex e acessado pelo Slack, com intenções de extrato, transferência, empréstimo e cancelamento de cartão.
*   **sprint-8-pb-aws-furg-ifrs-uffs-equipe-01:** Identifier, uma API que analisa imagens guardadas no S3 com o Amazon Rekognition (rota `POST /v1/vision`), com infraestrutura em Terraform.
*   **sprint-9-10-pb-aws-furg-ifrs-uffs-equipe-2:** EquiTalk Bot, um chatbot de acessibilidade com Amazon Lex, Polly, Transcribe e Rekognition, integrado ao WhatsApp via Twilio e publicado com Serverless.

## 🚀 Como Usar

Para explorar os projetos e atividades deste repositório, siga os passos abaixo:

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/RafaelMPinheiro/Repos-Compass.git
    ```
2.  **Navegue até a pasta da sprint desejada:**
    ```bash
    cd Repos-Compass/sprint-X-nome-da-sprint
    ```
3.  **Siga as instruções no `README.md` interno:** Cada pasta de sprint possui um `README.md` detalhado com instruções específicas para configurar e executar o projeto.

## 🤝 Como Contribuir

Contribuições são muito bem-vindas! Se você deseja adicionar novas sprints, corrigir descrições, melhorar a documentação ou qualquer outra melhoria, siga estas diretrizes:

1.  **Faça um Fork** deste repositório.
2.  **Crie uma nova branch** para sua feature ou correção:
    ```bash
    git checkout -b feature/sua-feature-ou-correcao
    ```
3.  **Realize suas alterações** e adicione as descrições necessárias.
4.  **Commit suas alterações** com uma mensagem clara e descritiva.
5.  **Envie suas alterações** para o seu fork:
    ```bash
    git push origin feature/sua-feature-ou-correcao
    ```
6.  **Abra um Pull Request** para o branch `main` deste repositório, descrevendo suas alterações.

## 📄 Licença

Este projeto está licenciado sob a licença [MIT License](https://opensource.org/licenses/MIT). Sinta-se à vontade para usar, modificar e distribuir o código, desde que a licença seja mantida.

## 📧 Contato

Para dúvidas, sugestões ou contato, você pode encontrar Rafael M. Pinheiro em:

*   **GitHub:** [RafaelMPinheiro](https://github.com/RafaelMPinheiro)
*   **LinkedIn:** [Rafael M. Pinheiro](https://www.linkedin.com/in/rafaelmpinheiro/)

---

© 2025 Rafael M. Pinheiro. Todos os direitos reservados.




## 📊 Estatísticas e Badges

![GitHub last commit](https://img.shields.io/github/last-commit/RafaelMPinheiro/Repos-Compass)
![GitHub repo size](https://img.shields.io/github/repo-size/RafaelMPinheiro/Repos-Compass)
![GitHub language count](https://img.shields.io/github/languages/count/RafaelMPinheiro/Repos-Compass)
![GitHub top language](https://img.shields.io/github/languages/top/RafaelMPinheiro/Repos-Compass)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
