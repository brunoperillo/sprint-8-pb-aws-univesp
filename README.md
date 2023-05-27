# Avaliação Sprint 8 - Programa de Bolsas Compass UOL / AWS e Univesp

## Introdução

_Escrever uma breve introdução a respeito de funções lambda, regoknition e api gateway_

---

## Objetivo

Foi desenvolvida uma API que faz a detecção de rótulos ou de emoções em faces a partir de imagens colocadas no bucket S3, para isso são utilizadas:

* Funções Lambda que irão dar suporte às APIs

* API Amazon Rekognition que faz a detecção de rótulos e de faces

* Amazon CloudWatch onde são registrados os logs de chamadas da API

---

## Desenvolvimento

### Requisitos

* Conta AWS Web Services
* Ferramenta para requisições GET/POST

### Ferramentas e tecnologias utilizadas

* AWS Lambda para manipulação de funções
* AWS S3 Para armazenamento de imagens
* AWS API Gateway para requisições GET e POST
* AWS Regoknition para identificação de rótulos e faces

Clone este repositório e instale o [framework serverless](https://www.serverless.com/framework/docs/getting-started)

```bash
  npm install -g serverless
```

Gere suas [credenciais](https://www.serverless.com/framework/docs/providers/aws/guide/credentials/) (AWS Acess Key e AWS Secret) na console AWS pelo IAM.

Configure seu ambiente com as credenciais via AWS CLI

```bash
  $ aws configure
  AWS Access Key ID [None]: AKIAIOSFODNN7EXAMPLE
  AWS Secret Access Key [None]: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
  Default region name [None]: us-east-1
  Default output format [None]: ENTER
```

Altere o nome do BucketS3 no arquivo `serverless.yml` para um nome exclusivo.

Navegue até o diretório `visao_computavcional` e faça o deploy:

```bash
serverless deploy
```

Anote os endpoits para as rotas: /, /v1, /v2, /1/vision e /v2/vision

Manualmente, faça o envio dos arquivos de imagem para seu bucket recém criado.
Adicione essas permissões para que os arquivos no seu bucket estejam acessíveis publicamente:

```json
  {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadGetObject",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::<YOUR_BUCKET_NAME>/*"
        }
    ]
  }
```

---

## Execução

### GET /

Faça requisições para os endpoints obtidos após o deploy.

A rota raíz, ou /, deverá retornar uma mensagem como observado abaixo:

```json
  {
    "message": "Go Serverless v3.0! Your function executed successfully!",
    "input": {
      "event"
      }
  }
```

Posteriormente, faça também requisições para a rota /v1 e /v2 e confirme os resultados:

GET /v1

```json
  {
  "message": "VISION api version 1."
  }
```

GET /v2

```json
  {
  "message": "VISION api version 1."
  }
```

---

## Resultados

### POST /v1/vision

Faça requisições `POST` para a rota /v1/vision, inserindo no body da requisição o nome do bucket e o nome da imagem. Verifique o resltado conforme exemplo:

<div align="center">
  <img src="./assets/result_imgs/v1-vision.png">
  <a href="https://sprint-8-vision.s3.amazonaws.com/gato4.jpg" target="_blank">https://sprint-8-vision.s3.amazonaws.com/gato4.jpg</a>
</div>

---

### POST /v2/vision

Seguindo as mesmas instruções, envie requisições do tipo POST para a rota /v2/vision
Lembre-se de modificar o nome da imagem para referênciar uma imagem que possua rostos.

<div align="center">
  <img src="./assets/result_imgs/v2-vision.png">
  <a href="https://sprint-8-vision.s3.amazonaws.com/raiva.png" target="_blank">https://sprint-8-vision.s3.amazonaws.com/raiva.png</a>
</div>

<br>
Caso exista mais de um rosto na sua imagem, a resposta deverá ser retornada com um resultado para cada face, conforme observado no exemplo:

<div align="center">
  <img src="./assets/result_imgs/v2-vision-varias.png">
  <a href="https://sprint-8-vision.s3.amazonaws.com/varias_emocoes.jpg" target="_blank">https://sprint-8-vision.s3.amazonaws.com/varias_emocoes.jpg</a>
</div>

---

## Tratamento de erros

Caso a imagem passada para o Rekognition não possua nenhuma face, a resposta esperada deverá retornar os campos de `position` iguais "null" e código de erro igual a _500_, conforme exemplo:

<div align="center">
  <img src="./assets/result_imgs/v2-vision-null.png">
  <a href="https://sprint-8-vision.s3.amazonaws.com/gato4.jpg" target="_blank">https://sprint-8-vision.s3.amazonaws.com/gato4.jpg</a>
</div>

<br>

Neste caso passamos a imagem de um gato para o reconhecimento de faces, a resposta para as faces localizadas retornará `null`

Já quando fazemos envio de uma requisição com o body incorreto, a mensagem de erro com código _500_ deverá ser retornada:

<div align="center">
  <img src="./assets/result_imgs/v2-vision-error2.png">
  <sub>Envio de uma requisição com `json` incorreto</sub>
</div>

<br>

O envio de uma requisição com uma imagem não presente no bucket selecionado também retornará erro:

<div align="center">
  <img src="./assets/result_imgs/v2-vision-error.png">
  <sub>Arquivo não presente no bucket selecionado</sub>
</div>

## Conclusão

---

## Dificuldades

---

## Integrantes - Grupo 2

<div align="center">

  | [<img src="https://avatars.githubusercontent.com/u/97908745?v=4" width=115><br><sub>Ana Vitória</sub>](https://github.com/anaVitoriaLouro) | [<img src="https://avatars.githubusercontent.com/u/87142990?v=4" width=115><br><sub>Luciene Godoy</sub>](https://github.com/LucieneGodoy) |  [<img src="https://avatars.githubusercontent.com/u/72028902?v=4" width=115><br><sub>Luiz Sassi</sub>](https://github.com/luizrsassi) | [<img src="https://avatars.githubusercontent.com/u/73674662?v=4" width=115><br><sub>Marcos Vinicios</sub>](https://github.com/onativo)|
  | :---: | :---: | :---: |:---: |

</div>