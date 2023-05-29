# Avaliação Sprint 8 - Programa de Bolsas Compass UOL / AWS e Univesp

Avaliação da [Sprint 8][sprint8main] do Programa de Bolsas [Compass UOL][compass] para formação em *machine learning* com [AWS][aws]. [Diretrizes do pedido][sprint8main] 
***

<div align="center">
  <h1 style="font-size: 32px;"><b>Visão Computacional com AWS Rekognition</b></h1>
</div>


## Introdução
A visão computacional, também conhecida como reconhecimento visual ou percepção visual, é um campo de estudo que se concentra em permitir que os computadores obtenham uma compreensão de alto nível de imagens e vídeos digitais. Envolve o desenvolvimento de algoritmos e técnicas para extrair informações significativas e fazer inferências a partir de dados visuais.

Uma ferramenta poderosa no campo da visão computacional é o [AWS Rekognition][Amazon Rekognition], que oferece uma ampla variedade de recursos e funcionalidades. Ele permite que os desenvolvedores executem tarefas como análise de imagem e vídeo, detecção e reconhecimento de objetos, análise facial, análise de sentimentos e muito mais. Aproveitando modelos e APIs pré-treinados, os desenvolvedores podem integrar facilmente essas funcionalidades em seus aplicativos sem a necessidade de extensa experiência em aprendizado de máquina.

## Objetivo
Disponibilizar uma solução pronta para produção na AWS, capaz de receber requisições de imagens, extrair informações relevantes por meio do [AWS Rekognition][Amazon Rekognition] e retornar os resultados de forma estruturada, atendendo às especificações e formatos esperados para cada rota da API.

## Funcionamento
A solução utiliza o framework Serverless para criar um conjunto de lambdas que se integram ao [AWS Rekognition][Amazon Rekognition] e ao [S3][Amazon S3]. As lambdas são responsáveis por receber as requisições, processar as imagens e extrair as informações relevantes. Os resultados são retornados de acordo com o formato esperado para cada rota da API.

A arquitetura geral do projeto é a seguinte:

1. O usuário fornece uma imagem que é enviada para o serviço [S3][Amazon S3], que é um serviço de armazenamento de objetos da AWS.
2. O [API Gateway][API Gateway], que atua como ponto de entrada da aplicação, recebe a requisição HTTP com a imagem.
3. O [API Gateway][API Gateway] encaminha a requisição para a função [Lambda][Amazon Lambda] correspondente.
4. A função [Lambda][Amazon Lambda] é responsável por processar a imagem recebida e invocar o serviço [Rekognition][Amazon Rekognition] da AWS.
5. O serviço [Rekognition][Amazon Rekognition], utilizando técnicas de visão computacional, extrai informações da imagem, como rótulos (tags) que descrevem o conteúdo da imagem e emoções identificadas nas faces presentes na imagem.
6. A função [Lambda][Amazon Lambda] recebe a resposta do [Rekognition][Amazon Rekognition] e realiza o log dos resultados no serviço [CloudWatch][Amazon CloudWatch].
7. A resposta final contendo as informações processadas é retornada ao [API Gateway][API Gateway].
8. O [API Gateway][API Gateway] envia a resposta ao usuário que fez a requisição.

Dessa maneira essa será a arquitetura a ser impantada em TODA ATIVIDADE será:

<p align="center">
  <img src="./assets/arquitetura-base.png" alt="arquitetura-base" width="800">
</p>



## Requisitos
- Node.js (versão 10 ou superior)
- Acesso à AWS (para implantar a solução)
- AWS CLI configurado com as credenciais adequadas (opcional)

## Instalação e Implantação
1. Clone este repositório
Clone o repositório do projeto em seu ambiente local usando o comando:
```bash
git clone https://github.com/Compass-pb-aws-2023-Univesp/sprint-8-pb-aws-univesp.git
```
2. Navegue até o diretório do projeto:
Use o comando cd para navegar até o diretório do projeto:
```bash
cd sprint-8-pb-aws-univesp/visao-computacional
```

3. Instale as [dependências][Serverless Framework] do projeto:
Certifique-se de ter o Node.js instalado em sua máquina (versão 10 ou superior).
Instale o Serverless Framework globalmente usando o seguinte comando:
```bash
npm install -g serverless
```
4. Configurar as [credenciais da AWS][Credenciais AWS]:
- Acesse o Console de Gerenciamento da AWS e crie um usuário do IAM com permissões adequadas para acessar os serviços necessários (Lambda, S3, Rekognition, CloudWatch, IAM).
- Anote a chave de acesso e a chave secreta geradas para o usuário do IAM.

5. Configurar as credenciais localmente:
Abra o terminal e execute o seguinte comando:
```bash
serverless config credentials --provider aws --key SUA_ACCESS_KEY --secret SUA_SECRET_KEY
```
Substitua "SUA_ACCESS_KEY" e "SUA_SECRET_KEY" pelas suas próprias credenciais do IAM.

6. Implante a solução na AWS:
```bash
serverless deploy
```
7. Após a implantação, você receberá informações sobre os endpoints disponíveis. Anote essas informações para uso posterior.

O projeto é dividido em duas partes, com rotas diferentes, nomeadamente de Parte 1 e Parte 2


## Estrutura do projeto
O projeto segue a estrutura padrão do framework Serverless e está organizado da seguinte forma:

- serverless.yml: arquivo de configuração do Serverless Framework, que define as funções Lambda, eventos, políticas de permissão e outros recursos.
- src/: diretório contendo o código-fonte das lambdas.
- src/handlers/: diretório contendo os manipuladores das requisições.
- src/services/: diretório contendo os serviços auxiliares, como integração com o [Rekognition][Amazon Rekognition] e [S3][Amazon S3].

## Implementação da solução

### > **Detecção de rótulos** (Rota /v1/vision)

A partir de uma função Lambda em python associada à rota, o Rekognition é acionado para detecção de rótulos na imagem salva num bucket do S3.

Formato da requisição (POST):

```json
{
  "bucket": "mycatphotos",
  "imageName": "cat.jpg"
}
```

Exemplos de resultados obtidos (como definido no padrão informado, são apresentados somente os quatro primeiros rótulos, os com maior índice de confiança):

<table>
  <tr>
    <td>
      <img src="https://github.com/Compass-pb-aws-2023-Univesp/sprint-8-pb-aws-univesp/blob/grupo-1/assets/cat2.jpg?raw=true" width="60%"> 
    </td>
    <td>
      <img src="https://github.com/Compass-pb-aws-2023-Univesp/sprint-8-pb-aws-univesp/blob/grupo-1/assets/cat1_labels.png?raw=true" alt="Detecção rotulos gato" width="100%">
    </td>
  </tr>
</table>

<table>
  <tr>
    <td>
      <img src="https://github.com/Compass-pb-aws-2023-Univesp/sprint-8-pb-aws-univesp/blob/grupo-1/assets/dog1.png?raw=true" alt="Foto cachorro" width="72%"> 
    </td>
    <td>
      <img src="https://github.com/Compass-pb-aws-2023-Univesp/sprint-8-pb-aws-univesp/blob/grupo-1/assets/dog1_labels.png?raw=true" alt="Rotulos dog" width="90%">
    </td>
  </tr>
</table>

Exemplo de uma requisição com erro (imagem não existe no bucket):

<div align="center">
  <img src="https://github.com/Compass-pb-aws-2023-Univesp/sprint-8-pb-aws-univesp/blob/grupo-1/assets/erro.png?raw=true" alt="Requisição inválida" width="60%"/>
</div>

<br></br>

### Detecção facial (Rota /v2/vision)

Foi criada uma função em python para acessar uma imagem salva num bucket do S3, acionar o Rekognition para análise facial, e retornar o *bounding box* da(s) face(s) detectada(s) e a expressão facial de maior índice de confiança.

Formato da requisição (POST):

```json
{
  "bucket": "myphotos",
  "imageName": "test-happy.jpg"
}
```

Exemplos de resultados obtidos:

<table>
  <tr>
    <td>
      <div style="text-align: center;"><img src="https://avatars.githubusercontent.com/u/25699466?v=4" alt="Foto Bruno" width="100%"><p style="margin: 0 auto; font-size: 24px; text-align: center;"><a href="https://github.com/brunoperillo" target="_blank">Bruno Monserrat Perillo</a>
    </p>
</div>
    </td>
    <td>
      <img src="https://github.com/Compass-pb-aws-2023-Univesp/sprint-8-pb-aws-univesp/blob/grupo-1/assets/analise_facial_bruno.png?raw=true" alt="Analise facial Bruno" width="90%">
    </td>
  </tr>
</table>

<table>
  <tr>
    <td>
      <div style="text-align: center;"><img src="https://avatars.githubusercontent.com/u/81330043?v=4" alt="Foto Bernardo" width="100%"><p style="margin: 0 auto; font-size: 24px; text-align: center;"><a href="https://github.com/belima93"target="_blank">Bernardo Lima</a></p></div>
    </td>
    <td>
      <img src="https://github.com/Compass-pb-aws-2023-Univesp/sprint-8-pb-aws-univesp/blob/grupo-1/assets/analise_facial_bernardo.png?raw=true" alt="Analise facial Bernardo" width="90%">
    </td>
  </tr>
</table>

<table>
  <tr>
    <td>
      <div style="text-align: center;"><img src="https://avatars.githubusercontent.com/u/78061851?v=4" alt="Foto Carlos" width="100%"><p style="margin: 0 auto; font-size: 24px; text-align: center;"><a href="https://github.com/crobertocamilo" target="_blank">Carlos Roberto Camilo</a></p></div>
    </td>
    <td>
      <img src="https://github.com/Compass-pb-aws-2023-Univesp/sprint-8-pb-aws-univesp/blob/grupo-1/assets/analise_facial_carlos.png?raw=true" alt="Analise facial Carlos" width="90%">
    </td>
  </tr>
</table>

<table>
  <tr>
    <td>
      <div style="text-align: center;"><img src="https://avatars.githubusercontent.com/u/94749597?v=4" alt="Foto O'Dhara" width="100%"><p style="margin: 0 auto; font-size: 24px; text-align: center;"><a href="https://github.com/odharamaggi" target="_blank">O'Dhara Maggi</a></p></div>
    </td>
    <td>
      <img src="https://github.com/Compass-pb-aws-2023-Univesp/sprint-8-pb-aws-univesp/blob/grupo-1/assets/analise_facial_odhara.png?raw=true" alt="Analise facial O'Dhara" width="90%">
    </td>
  </tr>
</table>

## Organização
O projeto foi desenvolvido em equipe, com a divisão de responsabilidades entre os integrantes. O README.md foi escrito de forma objetiva e clara para facilitar a compreensão do projeto.

## Ferramentas utilizadas
- [AWS][aws] ([Lambda][Amazon Lambda], [S3][Amazon S3], [Rekognition][Amazon Rekognition], [API Gateway][API Gateway], [CloudWatch][Amazon CloudWatch] e [IAM][Amazon IAM])
- [Serverless Framework][Serverless Framework]
- VSCode
- GitHub

## Dificuldades Conhecidas

## Referências
- [AWS Rekognition][Amazon Rekognition]
- [AWS S3][Amazon S3]
- [AWS IAM][Amazon IAM]
- [AWS Lambda][Amazon Lambda]
- [AWS CloudWatch][Amazon CloudWatch]
- [API Gateway][API Gateway]
- [Serverless Framework][Serverless Framework]
- [Credenciais AWS][Credenciais AWS]
- <https://github.com/rjsabia/captionApp> (JS)
- <https://docs.aws.amazon.com/pt_br/rekognition/latest/dg/labels.html> (Trabalhando com Rótulos)
- <https://docs.aws.amazon.com/pt_br/rekognition/latest/dg/service_code_examples.html> (Exemplos de código)
- <https://docs.aws.amazon.com/rekognition/latest/dg/faces-detect-images.html> (Trabalhando com Faces)
- <https://docs.aws.amazon.com/pt_br/rekognition/latest/dg/service_code_examples.html> (Exemplos de código)

----------

## Desenvolvedores do projeto
| [<img src="https://avatars.githubusercontent.com/u/81330043?v=4" width=115><br><sub>Bernardo Lima</sub>](https://github.com/belima93) | [<img src="https://avatars.githubusercontent.com/u/25699466?v=4" width=115><br><sub>Bruno Monserrat Perillo</sub>](https://github.com/brunoperillo) |  [<img src="https://avatars.githubusercontent.com/u/78061851?v=4" width=115><br><sub>Carlos Roberto Camilo</sub>](https://github.com/crobertocamilo) | [<img src="https://avatars.githubusercontent.com/u/94749597?v=4" width=115><br><sub>O'Dhara Maggi</sub>](https://github.com/odharamaggi)|
| :---: | :---: | :---: |:---: |

   [compass]: <https://compass.uol/en/home/>
   [aws]: <https://aws.amazon.com/pt/>
   [sprint8main]: <https://github.com/Compass-pb-aws-2023-Univesp/sprint-8-pb-aws-univesp/tree/main>
   [Amazon Rekognition]: <https://aws.amazon.com/pt/rekognition/>
   [Amazon S3]: <https://aws.amazon.com/pt/s3/>
   [Amazon IAM]: <https://aws.amazon.com/pt/iam/>
   [API Gateway]: <https://aws.amazon.com/pt/api-gateway>
   [Amazon Lambda]: <https://aws.amazon.com/pt/lambda/>
   [Amazon CloudWatch]: <https://aws.amazon.com/pt/cloudwatch/>
   [Serverless Framework]: <https://www.serverless.com/framework/docs/getting-started>
   [Credenciais AWS]: <https://www.serverless.com/framework/docs/providers/aws/guide/credentials/>
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
