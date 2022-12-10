# Projeto 6: Visão Computacional e utilização de APIs

Introdução ao uso de periféricos embarcados na raspberry com o uso do módulo de câmera, além da utilização do versionamento de código via Git/GitHub, e o uso de APIs para obtenção de dados da internet para o desenvolvimento de uma aplicação climática. 

---

## Objetivos

- [x] Utilizar o módulo de câmera da raspberry PI para captura de imagens e vídeos.
- [x] Utilizar o versionamento de código via Git/GitHub.
- [x] Utilizar APIs para obtenção de dados da internet.

## Descrição

Introdução ao uso de periféricos embarcados na raspberry com o uso do módulo de câmera, além da utilização do versionamento de código via Git/GitHub, e o uso de APIs para obtenção de dados da internet para o desenvolvimento de uma aplicação climática. A primeira parte da prática é referente ao uso da camera, enquanto a segunda é a da API climática. 

## Visão Computacional com a RaspCam

Com a camera conectada na raspberry e comunicação I2C habilitada, através do código disponível no arquivo "Pratica6.py" foi possível acessar as imagens da camera. Perceba que foi utilizado a biblioteca PiCamera para esse projeto. O output da camera obtido em laboratório pode ser visualizado abaixo:

<img src="sel0337.jpg" width=300>

Mesmo com a imagem "borrada", é perceptível que o sistema e os códigos funcionam como esperado. 

## API Climática

Obtenção de dados climáticos por meio da API de clima da Oracle, para isso, será utilizado as bibliotecas json e requests. O código completo pode ser encontrado no arquivo "Pratica6.py". A estação mais próxima para obtenção dos dados não fornecia as informações necessárias, por isso, utilizou-se a segunda mais perto, a qual possui dados para serem utilizados. O Output do código pode ser visto abaixo, onde é possível identificar no formato json, os dados obtidos pela API.

<img src="output.jpg" width=300>