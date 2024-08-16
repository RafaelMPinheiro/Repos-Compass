# Avaliação Sprint 1
## _Programa de Bolsas Compass_

Construção de um sistema de verificação de PIN (Personal Identification Number).

## Desafios

- solicite ao usuário que insira um número;
    -  Utilizei o prompt para solicitação do número;
- verifique se o número inserido é maior ou menor que o valor esperado (que pode ser fixo ou randômico);
    -  Utilizei um número fixo para melhor testes;
- caso seja o valor correto, imprima na tela uma mensagem de parabéns;
- caso contrário, indique ao usuário se o próximo valor deve ser maior, muito maior, menor ou muito menor que o informado.
    - Utilizei if-else para determinar qual dica ajudaria mais o usuário: 
        - Muito maior - tentativa > 1.5 * número
        - Maior - tentativa > número
        - Menor - tentativa < número
        - Muito menor - tentativa < 0.5 * número

## Installation

Para mais simples visualização foi usado a extensão Live Server.

```sh
git clone https://github.com/Compass-pb-aws-2023-FURG-IFRS-UFFS/sprint-1-pb-aws-furg-ifrs-uffs.git
cd sprint-1-pb-aws-furg-ifrs-uffs
git branch -a
git checkout rafael-pinheiro
Ative o Live Server
```