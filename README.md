# JobScrapping

[![JobScrapping API](https://github.com/leonardosblang/job-scrapping-api/actions/workflows/python-app.yml/badge.svg)](https://github.com/leonardosblang/job-scrapping-api/actions/workflows/python-app.yml)

<img src="https://user-images.githubusercontent.com/61352086/194158541-07e551e3-8fd1-4289-b16f-eebf5afb3fad.png" alt="made by lang" style="width: 100px; height: 100px;"/>

## 🚀 Descrição 🚀

O projeto JobScrapping é busca coletar as informações de vagas de emprego em diversos sites e enviar essas informações para um banco de dados (MongoDB). Este banco será consultado por uma API em Python que disponibilizará essas informações em um formato JSON para o app (PWA - _Progressive Web Apps_) em React.

## API e Testes Unitários da API JobScrapping

### Pré-Requisitos

O principal pré-requisito é o [Python](https://www.python.org/).

### Instalando as Dependências

```bash
pip install fastapi
pip install uvicorn[standard]
pip install pymongo
```

### Rodando a API

```bash
uvicorn main:app
```

### Executando os Testes

```bash
python -m unittest
```

## Autores do Projeto

- [George Luis Costa Ribeiro](https://github.com/George-Luis-Costa)
- [Bruno Almeida Vasconcelos](http://github.com/brunovollin)
- [Leonardo S. B. Lang](https://github.com/leonardosblang)
- [Fabio Neto](https://github.com/bio353)
