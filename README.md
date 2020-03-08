# Desenvolvimento de API com Flask


API para definir quais notas e moedas tem que ser dada para troco de uma compra.
API desenvolvida com python3.6, Flask e mongodb.

## Table of Contents:

- [Requisitos](#requisitos)
- [Setup](#setup)
- [API](#api)
- [Web](#web)
- [Database](#database)

## Requisitos

- Python 3.6
- Flask 1.1.1
- MondoDB Server 4.2.3
- Database criado com o nome "localdb"
- Virtualenv

## Setup

- Efetuar o clone do repositório da aplicação.
- Criar um ambiente virtual usando o virutalenv.
- Ativar o ambiente virtual.
- Efetuar a instalação dos requirements do arquivo "requirements.txt".
- Efetuar o start da aplicação executando o comando "python run.py"

## API

- Foi criado um unico endpoint para o calculo do troco.
- Aguarda um POST contendo um Json no body da request contendo os valores de pagamento e valor da compra.
- A URL do endpoint é: http://localhost:5000/api/controle_troco
- Efetuando a request como POST deve ser passado no body o seguinte Json: {"valor_pago":valor_pago, "valor_total":valor_total}.
- Efetuando a request como GET apensa retorna um Json informando o metodo usado.

## Web

- Foi criada uma pagina web para efetuar a chamada da API informando os valores necessários.
- É necessário informar os valores do formulário.
- A URL do endpoint é: http://localhost:5000/

## Database

- Utilizado o banco MongoDB.
- Foi criado uma collection para registrar todas as transações efetuadas através da API.
