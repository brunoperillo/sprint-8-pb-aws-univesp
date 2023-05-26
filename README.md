# Avaliação Sprint 8 - Programa de Bolsas Compass UOL / AWS e Univesp

  

## Introdução

_Escrever uma breve introdução a respeito de funções lambda, regoknition e api gateway_

  

---

## Objetivo

  

Foi desenvolvida uma API que faz a detecção de rótulos ou de emoções em faces a partir de imagens colocadas no bucket S3, para isso são utilizadas:

* Funções Lambda que irão dar suporte às APIs

* API Amazon Rekognition que faz a detecção de rótulos e de faces

* Amazon CloudWatch onde são registrados os logs de chamadas da API

  

## Desenvolvimento

  

---

## Execução

---

Para utilizar a API é necessária uma conta na AWS e o uso de uma ferramenta para chamada e leitura da API como o Postman.

  

*    Usando a rota Post /v1/vision

1.   Realizar o git clone desse repo

2.   Ter o framework Serverless instalado no computador

3.   Modificar o nome do Bucket S3 no arquivo visao-computacional/serverless.yml, a propriedade BucketName contém o nome do Bucket que deve ser único na AWS

4.   Para fazer o deploy da solução na sua conta aws execute o código a seguir na pasta visao-computacional

```bash

serverless deploy

```

5.   Após o deploy serão retornados os endpoints, para uso dos endpoints GET [clique aqui]() o uso dos demais segue na sequência

6.   Inicie o Postman e numa nova guia selecione a opção POST e digite o endpoint da rota /v1/vision na barra, selecione Body, raw e troque Text por JSON

7.   No corpo da requisição coloque uma entrada conforme exemplo

```json

{

  "bucket": "minhasImagens",

  "imageName": "catdog.jpg"

}

```

8.   Você receberá uma resposta parecida com a seguinte

```json

{

    "url_to_image": "https://bucketbucket.s3.amazonaws.com/catdog.jpg",

    "created_image": "26-05-2023 18:51:59",

    "labels": [

        {

            "confidence": 99.9623031616211,

            "Name": "Canine"

        },

        {

            "confidence": 99.9623031616211,

            "Name": "Dog"

        },

        {

            "confidence": 99.9623031616211,

            "Name": "Pet"

        },

        {

            "confidence": 99.9623031616211,

            "Name": "Puppy"

        }

    ]

}

  

```

  

*    Usando a rota Post /v2/vision

1.    Seguir as mesmas etapas de 1 a 5 acima

2.    Inicie o Postman e numa nova guia selecione a opção POST e digite o endpoint da rota /v2/vision na barra, selecione Body, raw e troque Text por JSON

3.    No corpo da requisição coloque uma entrada conforme exemplo

```json

{

  "bucket": "minhasImagens",

  "imageName": "happy.jpg"

}

```

4.    Você receberá uma resposta parecida com a seguinte

```json

{

    "url_to_image": "https://bucketbucket.s3.amazonaws.com/happy.jpg",

    "created_image": "26-05-2023 18:53:17",

    "faces": [

        {

            "position": {

                "Height": 0.8282204270362854,

                "Left": 0.2988795042037964,

                "Top": 0.1413968801498413,

                "Width": 0.4000350534915924

            },

            "classified_emotion": "HAPPY",

            "classified_emotion_confidence": 90.8899154663086

        }

    ]

}

```

5.    Caso tenham mais imagens será retornada uma lista como a mostrada a seguir

```json

{

    "url_to_image": "https://bucketbucket.s3.amazonaws.com/varias_emocoes.jpg",

    "created_image": "26-05-2023 18:54:29",

    "faces": [

        {

            "position": {

                "Height": 0.31912365555763245,

                "Left": 0.4293184280395508,

                "Top": 0.6375865340232849,

                "Width": 0.15741190314292908

            },

            "classified_emotion": "SURPRISED",

            "classified_emotion_confidence": 99.68412780761719

        },

        {

            "position": {

                "Height": 0.32064223289489746,

                "Left": 0.4283589720726013,

                "Top": 0.0901685580611229,

                "Width": 0.15306353569030762

            },

            "classified_emotion": "ANGRY",

            "classified_emotion_confidence": 99.94093322753906

        },

        {

            "position": {

                "Height": 0.30503055453300476,

                "Left": 0.7665966153144836,

                "Top": 0.05946614220738411,

                "Width": 0.1547987014055252

            },

            "classified_emotion": "HAPPY",

            "classified_emotion_confidence": 99.85910034179688

        },

        {

            "position": {

                "Height": 0.2805452346801758,

                "Left": 0.09599878638982773,

                "Top": 0.06656099855899811,

                "Width": 0.15971219539642334

            },

            "classified_emotion": "CALM",

            "classified_emotion_confidence": 99.76969146728516

        },

        {

            "position": {

                "Height": 0.2778734266757965,

                "Left": 0.7582355737686157,

                "Top": 0.6446410417556763,

                "Width": 0.15722627937793732

            },

            "classified_emotion": "CONFUSED",

            "classified_emotion_confidence": 92.0582275390625

        },

        {

            "position": {

                "Height": 0.27487388253211975,

                "Left": 0.09735958278179169,

                "Top": 0.6502690315246582,

                "Width": 0.15286672115325928

            },

            "classified_emotion": "SAD",

            "classified_emotion_confidence": 60.7897834777832

        }

    ]

}

  

```

  

## Resultados

---

## Conclusão

---

## Dificuldades

  

---

## Integrantes - Grupo 2

  

<div align="center">

  

  | [<img src="https://avatars.githubusercontent.com/u/97908745?v=4" width=115><br><sub>Ana Vitória</sub>](https://github.com/anaVitoriaLouro) | [<img src="https://avatars.githubusercontent.com/u/87142990?v=4" width=115><br><sub>Luciene Godoy</sub>](https://github.com/LucieneGodoy) |  [<img src="https://avatars.githubusercontent.com/u/72028902?v=4" width=115><br><sub>Luiz Sassi</sub>](https://github.com/luizrsassi) | [<img src="https://avatars.githubusercontent.com/u/73674662?v=4" width=115><br><sub>Marcos Vinicios</sub>](https://github.com/onativo)|

  | :---: | :---: | :---: |:---: |

  

</div>

  

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