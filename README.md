## Avaliação Sprint 8 - Programa de Bolsas Compass UOL / AWS e Univesp

Avaliação da [Sprint 8][sprint8main] do Programa de Bolsas [Compass UOL][compass] para formação em *machine learning* com [AWS][aws]. [Diretrizes do pedido][sprint8main] 
***

<div align="center">
  <h1 style="font-size: 32px;"><b>Visão Computacional com AWS Rekognition</b></h1>
</div>

<p align="center">
  <img src="/assets/rekog.png" alt="título" width="600">
</p>


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
1. Clone este repositório;
2. Navegue até o diretório do projeto;
3. Instale as [dependências][Serverless Framework] do projeto:

Certifique-se de ter o Node.js instalado em sua máquina (versão 10 ou superior).
Instale o Serverless Framework globalmente usando o seguinte comando:
```bash
npm install -g serverless
```
4. Configure as [credenciais da AWS][Credenciais AWS] localmente utilizando a *key* e a *secret key* geradas para o usuário no IAM:
Abra o terminal e execute o seguinte comando:
```bash
serverless config credentials --provider aws --key SUA_ACCESS_KEY --secret SUA_SECRET_KEY
```
5. Faça o *deploy* do projeto na AWS:
```bash
serverless deploy
```
6. Se a instalação for bem sucedida, serão exibidos os *endpoints* gerados no API Gateway e o nome do bucket gerado no S3 (caso não ainda não existisse), como exemplificado na imagem abaixo:

<div align="center">
  <img src="https://github.com/Compass-pb-aws-2023-Univesp/sprint-8-pb-aws-univesp/blob/grupo-1/assets/deploy.png?raw=true" alt="endpoints gerados" width="60%"/>
</div>
   
7. Faça o upload das imagens para os buckets no S3;

8. Para testar a API, utilize, por exemplo o [**Postman**](https://www.postman.com/), ou a função de teste de rotas no console do API Gateway no site da AWS. O padrão das requisições deve respeitar o formato informado nas seções abaixo.


## Estrutura do projeto
O projeto segue a estrutura padrão do Serverless Framework e está organizado da seguinte forma:

- serverless.yml: arquivo de configuração do Serverless Framework, que define as funções Lambda, eventos, políticas de permissão e outros recursos;
- src/: diretório contendo o código-fonte das funções Lambdas (a linguagem de programação utilizada foi python);
- assets/: diretório com imagens utilizadas para testes da API e prints dos resultados das análises.

## Implementação da solução

###  **Detecção de rótulos** (Rota /v1/vision)
<br>

A partir de uma função Lambda em python associada à rota, o Rekognition é acionado para detecção de rótulos na imagem salva num bucket do S3.

Formato da requisição (POST):

```json
{
  "bucket": "mycatphotos",
  "imageName": "cat.jpg"
}
```

Como definido no padrão informado, são apresentados somente os quatro primeiros rótulos (que possuem os maiores índices de confiança).

Exemplo dos resultados obtidos:

<table>
  <tr>
    <td>
      <div style="text-align: center;"><img src="https://github.com/Compass-pb-aws-2023-Univesp/sprint-8-pb-aws-univesp/raw/grupo-1/assets/cat4.jpg" alt="Gato" width="250">
    </td>
    <td>
      <img src="https://github.com/Compass-pb-aws-2023-Univesp/sprint-8-pb-aws-univesp/raw/grupo-1/assets/cat4_labels.png" alt="Rótulo Gato" width="500">
    </td>
  </tr>
</table>

<table>
  <tr>
    <td>
      <div style="text-align: center;"><img src="https://github.com/Compass-pb-aws-2023-Univesp/sprint-8-pb-aws-univesp/raw/grupo-1/assets/dog1.png" alt="Gato" width="250">
    </td>
    <td>
      <img src="https://github.com/Compass-pb-aws-2023-Univesp/sprint-8-pb-aws-univesp/raw/grupo-1/assets/dog1_labels.png" alt="Rótulo Gato" width="500">
    </td>
  </tr>
</table>

Requisição de imagem inexistente no bucket:

![Erro](/assets/erro.png)

<br>

### **Detecção facial** (Rota /v2/vision)
<br>

Foi criada uma função em Python para acessar uma imagem salva num bucket do S3, acionar o Rekognition para análise facial, e retornar o *bounding box* da(s) face(s) detectada(s) e a expressão facial de maior índice de confiança.

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
      <div style="text-align: right;"><img src="https://avatars.githubusercontent.com/u/25699466?v=4" alt="Foto Bruno" width="100%"><p style="margin: 0 auto; font-size: 10px; text-align: center;"><a href="https://github.com/brunoperillo" target="_blank"></a>
    </p>
</div>
    </td>
    <td>
      <img src="https://github.com/Compass-pb-aws-2023-Univesp/sprint-8-pb-aws-univesp/blob/grupo-1/assets/analise_facial_bruno.png?raw=true" alt="Analise facial Bruno" width="900">
    </td>
  </tr>
</table>

<table>
  <tr>
    <td>
      <div style="text-align: center;"><img src="https://avatars.githubusercontent.com/u/81330043?v=4" alt="Foto Bernardo" width="100%"><p style="margin: 0 auto; font-size: 24px; text-align: center;"><a href="https://github.com/belima93"target="_blank"></a></p></div>
    </td>
    <td>
      <img src="https://github.com/Compass-pb-aws-2023-Univesp/sprint-8-pb-aws-univesp/blob/grupo-1/assets/analise_facial_bernardo.png?raw=true" alt="Analise facial Bernardo" width="900">
    </td>
  </tr>
</table>

<table>
  <tr>
    <td>
      <div style="text-align: center;"><img src="https://avatars.githubusercontent.com/u/78061851?v=4" alt="Foto Carlos" width="100%"><p style="margin: 0 auto; font-size: 24px; text-align: center;"><a href="https://github.com/crobertocamilo" target="_blank"></a></p></div>
    </td>
    <td>
      <img src="https://github.com/Compass-pb-aws-2023-Univesp/sprint-8-pb-aws-univesp/blob/grupo-1/assets/analise_facial_carlos.png?raw=true" alt="Analise facial Carlos" width="900">
    </td>
  </tr>
</table>

<br></br>
### Múltiplas faces numa mesma imagem:
<br>

<div align="center">
  <img src="https://github.com/Compass-pb-aws-2023-Univesp/sprint-8-pb-aws-univesp/blob/grupo-1/assets/multiple_faces.png?raw=true" width="70%"/>
</div>
<br>
<div align="center">
  <img src="https://github.com/Compass-pb-aws-2023-Univesp/sprint-8-pb-aws-univesp/blob/grupo-1/assets/analise_facial_odhara-multiple_faces.png?raw=true" width="100%"/>
</div>

<br>

### Nenhuma face na imagem:
<br>

<table>
  <tr>
    <td>
      <div style="text-align: center;"><img src="https://github.com/Compass-pb-aws-2023-Univesp/sprint-8-pb-aws-univesp/blob/grupo-1/assets/no_faces.jpg?raw=true" alt="Sem faces" width="200">
    </td>
    <td>
      <img src="https://github.com/Compass-pb-aws-2023-Univesp/sprint-8-pb-aws-univesp/blob/grupo-1/assets/analise_facial-no_faces.png?raw=true" alt="Análise facial - sem faces" width="500">
    </td>
  </tr>
</table>


## Organização
O projeto foi desenvolvido em equipe, com a divisão de responsabilidades entre os integrantes. O README.md foi escrito de forma objetiva e clara para facilitar a compreensão do projeto.

## Ferramentas utilizadas
- [AWS][aws] ([Lambda][Amazon Lambda], [S3][Amazon S3], [Rekognition][Amazon Rekognition], [API Gateway][API Gateway], [CloudWatch][Amazon CloudWatch] e [IAM][Amazon IAM])
- [Serverless Framework][Serverless Framework]
- [VSCode](https://code.visualstudio.com/)
- [GitHub](https://github.com/)

## Dificuldades Conhecidas

- Desenvolvimento do código

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
