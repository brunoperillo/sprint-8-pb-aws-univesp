# Avaliação Sprint 8 - Programa de Bolsas Compass UOL / AWS e Univesp
###  Programa de Bolsas Compass UOL - Formação em Machine Learning com AWS
***
<div align="center">
 <img src= "https://github.com/Compass-pb-aws-2023-Univesp/sprint-8-pb-aws-univesp/assets/88354075/64187a38-281e-4287-afcc-dd9ec97be1ff" alt="capa github" 
  width="450"/>
</div>



***
 
## Introdução 

Nessa Sprint foram abordados os serviços das *funções Lambda*, o *Rekognition*, *CloudWatch* e *API Gateway*. 

Com as funções Lambda são uma forma de executar código sem precisar gerenciar servidores, o Rekognition é um serviço de análise de imagem e vídeo baseado em aprendizado de máquina
(para esse projeto foi usado apenas imagens), e o API Gateway é uma plataforma para criar, gerenciar e proteger APIs. O CloudWatch foi utilizado para monitorar e registrar métricas, logs e eventos em tempo real, fornecendo insights sobre o desempenho dos recursos e serviços da AWS.

Esses serviços, quando combinados, permitem o desenvolvimento de aplicativos escaláveis, seguros
e com recursos avançados de análise visual.




****

## Objetivo

É criar rotas para APIs poderem trabalhar com o serviços Rekognition, trazendo informações das imagens carregadas no buket S3.
***

## Funcionamento 

Para usar o Amazon Rekognition, é necessário formatar corretamente os campos de entrada e saída da API, além de definir os códigos de status adequados para sucesso e erro. 
 *imagem da funçãoo


Os dados da imagem são enviados no corpo da solicitação como um JSON, com o campo Image contendo um objeto Bytes que contém os bytes da imagem. 
A resposta da API será verificada quanto ao código de status HTTP.

Se for 200, a solicitação foi bem-sucedida e o resultado é impresso. Caso contrário, um erro ocorreu e o código de status e o conteúdo da resposta são impressos.

****

## Organização

*** 

## Dificuldades Conhecidas


## Desenvolvedores do projeto

||<br><sub>  [<img src="https://avatars.githubusercontent.com/u/96358027?v=4"  width=115><br><sub>Diego Lopes </sub>](https://github.com/Diegox0301) | [<img src="https://avatars.githubusercontent.com/u/124359272?v=4" width=115><br><sub>Irati Gonçalves Maffra</sub>](https://github.com/IratiMaffra) | [<img src="https://avatars.githubusercontent.com/u/88354075?v=4" width=115><br><sub>Kelly Patricia Lopes Silva</sub>](https://github.com/KellyPLSilva) | [<img src="https://avatars.githubusercontent.com/u/117780664?v=4" width=115><br><sub>Viviane Alves</sub>](https://github.com/Vivianes86) |
| :---: | :---: | :---: |:---: |:---: |

