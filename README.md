# Avaliação Sprint 8 - Programa de Bolsas Compass UOL / AWS e Univesp

Avaliação da oitava sprint do programa de bolsas Compass UOL para formação em machine learning para AWS.


***

## Execução

Com base nas atividades anteriores realizadas, crie um conjunto de lambdas que irão dar suporte a APIs que irão rodar o "rekognition" para extrair tags de imagens postadas no S3, e também utilizaremos o CloudWatch para gravar os logs dos resultados.

**Especificações**:

A aplicação deverá ser desenvolvida com o framework 'serverless' e deverá seguir a estrutura que já foi desenvolvida neste repo.

Passo a passo para iniciar o projeto:

1. Crie a branch para o seu grupo e efetue o clone

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

```
$ aws configure
AWS Access Key ID [None]: AKIAIOSFODNN7EXAMPLE
AWS Secret Access Key [None]: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
Default region name [None]: us-east-1
Default output format [None]: ENTER
```

#### Observação

As credenciais devem ficar apenas localmente no seu ambiente. Nunca exponha as crendenciais no Readme ou qualquer outro ponto do codigo.

Após executar as instruções acima, o serverless estará pronto para ser utilizado e poderemos publicar a solução na AWS.

5. Para efetuar o deploy da solução na sua conta aws execute (acesse a pasta [visao-computacional](./visao-computacional) ):

```bash
serverless deploy
```

Depois de efetuar o deploy, vocẽ terá um retorno parecido com isso:

```bash
Deploying vision to stage dev (us-east-1)

Service deployed to stack vision-dev (85s)

endpoints:
  GET - https://xxxxxxxxxx.execute-api.us-east-1.amazonaws.com/
  GET - https://xxxxxxxxxx.execute-api.us-east-1.amazonaws.com/v1
  GET - https://xxxxxxxxxx.execute-api.us-east-1.amazonaws.com/v2
functions:
  health: vision-dev-health (2.1 kB)
  v1Description: vision-dev-v1Description (2.1 kB)
  v2Description: vision-dev-v2Description (2.1 kB)
```

6. Abra o browser e confirme que a solução está funcionando colando os 3 endpoints que deixamos como exemplo:

### Rota 1 → Get /

1. Esta rota já está presente no projeto
2. O retorno rota é:

```json
  {
    "message": "Go Serverless v3.0! Your function executed successfully!",
    "input": {
        ...(event)
      }
  }
```

3. Status code para sucesso da requisição será `200`

### Rota 2 → Get /v1

1. Esta rota já está presente no projeto
2. O retorno rota é:

```json
{
  "message": "VISION api version 1."
}
```

3. Status code para sucesso da requisição será `200`

### Rota 3 → Get /v2

1. Esta rota já está presente no projeto
2. O retorno rota é:

```json
{
  "message": "VISION api version 2."
}
```

---

Após conseguir rodar o projeto base o objetivo final será divida em três partes:

## Atividade -> Parte 1

### Rota 4 -> Post /v1/vision

Deverá ser criada a rota `/v1/vision` que receberá um post no formato abaixo:

```json
{
  "bucket": "mycatphotos",
  "imageName": "cat.jpg"
}
```

- Essa imagem deverá estar no S3 (faça o upload manualmente)
- Dessa forma esse post deverá chamar o rekognition para nos entregar o seguinte retorno
- O resultado (body) da chamada do Rekognition deverá ser logado na aplicação através do CloudWatch. utilize: `print(body)`

Resposta a ser entregue (exatamente neste formato):

```json
{
  "url_to_image": "https://mycatphotos/cat.jpg",
  "created_image": "02-02-2023 17:00:00",
  "labels": [
    {
      "Confidence": 96.59198760986328,
      "Name": "Animal"
    },
    {
      "Confidence": 96.59198760986328,
      "Name": "Cat"
    },
    {
      "Confidence": 96.59198760986328,
      "Name": "Pet"
    },
    {
      "Confidence": 96.59198760986328,
      "Name": "Siamese"
    }
  ]
}
```

Dessa maneira essa será a arquitetura a ser impantada em TODA ATIVIDADE será:

![arquitetura-base](./assets/arquitetura-base.png)

Exemplos e docs de referência:

- <https://github.com/rjsabia/captionApp> (JS)
- <https://docs.aws.amazon.com/pt_br/rekognition/latest/dg/labels.html> (Trabalhando com Rótulos)
- <https://docs.aws.amazon.com/pt_br/rekognition/latest/dg/service_code_examples.html> (Exemplos de código)

## Atividade -> Parte 2

### Rota 5 -> Post /v2/vision

Deverá ser criada a rota `/v2/vision` que receberá um post no formato abaixo:

```json
{
  "bucket": "myphotos",
  "imageName": "test-happy.jpg"
}
```

- Essa imagem deverá estar no S3 (faça o upload manualmente)
- Nesta versão deverão ser implementados novos campos de retorno que definirá qual a EMOÇÃO PRINCIPAL classificada pelo modelo (maior confiança).
- Para isso utilize um dos modelos que identificam faces do rekognition.
- O resultado (body) da chamada do Rekognition deverá ser logado na aplicação através do CloudWatch. utilize: `print(body)`.
- Caso exista mais de uma face, fazer o retorno de cada uma.
- Dessa forma esse post deverá chamar o rekognition para nos entregar o seguinte retorno:

Resposta a ser entregue (exatamente neste formato):

```json
{
  "url_to_image": "https://myphotos/test.jpg",
  "created_image": "02-02-2023 17:00:00",
  "faces": [
    {
     "position":
     {
      "Height": 0.06333330273628235,
      "Left": 0.1718519926071167,
      "Top": 0.7366669774055481,
      "Width": 0.11061699688434601
     }
     "classified_emotion": "HAPPY",
     "classified_emotion_confidence": 99.92965151369571686
    }
 ]
}
```

No caso de duas faces:

```json
{
  "url_to_image": "https://myphotos/test.jpg",
  "created_image": "02-02-2023 17:00:00",
  "faces": [
    {
     "position":
     {
      "Height": 0.06333330273628235,
      "Left": 0.1718519926071167,
      "Top": 0.7366669774055481,
      "Width": 0.11061699688434601
     }
     "classified_emotion": "HAPPY",
     "classified_emotion_confidence": 99.92965151369571686
    },
     {
     "position":
     {
      "Height": 0.08333330273628235,
      "Left": 0.3718519926071167,
      "Top": 0.6366669774055481,
      "Width": 0.21061699688434601
     }
     "classified_emotion": "HAPPY",
     "classified_emotion_confidence": 98.92965151369571686
    }
 ]
}
```

Resposta a ser entregue quando não houver face (exatamente neste formato):

```json
{
  "url_to_image": "https://myphotos/test.jpg",
  "created_image": "02-02-2023 17:00:00",
  "faces": [
    {
     "position":
     {
      "Height": Null,
      "Left": Null,
      "Top": Null,
      "Width": Null
     }
     "classified_emotion": Null,
     "classified_emotion_confidence": Null
    }
 ]
}
```

Exemplos e docs de referência:

- <https://docs.aws.amazon.com/rekognition/latest/dg/faces-detect-images.html> (Trabalhando com Faces)
- <https://docs.aws.amazon.com/pt_br/rekognition/latest/dg/service_code_examples.html> (Exemplos de código)

---

## Observações retorno esperado

- os campos de entrada e saida deverão estar nos formatos e com os nomes apresentados.
- status code para sucesso da requisição será `200`
- status code para erros deverá ser `500`


***

## O que será avaliado?

- Projeto em produção na AWS
- Em Python conforme projeto base disponibilizado
- Seguir as atividades na ordem proposta
- Sobre as rotas:
  - Possuir em cada rota os retornos esperados (somente campos solicitados e **exatamente** no formato conforme especificação)
- Infra-estrutura como código (evite ações manuais na console)
- Organização geral do código fonte
  - Estrutura de pastas
  - Estrutura da logica de negócio
  - Divisão de responsabilidades em arquivos/pastas distintos
  - Otimização do código fonte (evitar duplicações de código)
- Objetividade do README.md

***

## Entrega

- Aceitar o convite do repositório da sprint-8-pb-aws-univesp;
- **O trabalho deve ser feito em grupos de 4 integrantes**;
  - Não repetir formação de grupos já criados em sprints anteriores;
- Criar uma branch no repositório com o formato grupo-número (Exemplo: grupo-1);
- Subir o trabalho na branch com um README.md;
  - Documentar detalhes sobre como a avaliação foi desenvolvida;
  - Dificuldades conhecidas;
  - Como utilizar o sistema;
- O prazo de entrega é até às 12h do dia 29/05/2023 no repositório do github ([https://github.com/Compass-pb-aws-2023-Univesp/sprint-8-pb-aws-univesp](https://github.com/Compass-pb-aws-2023-Univesp/sprint-8-pb-aws-univesp)).
