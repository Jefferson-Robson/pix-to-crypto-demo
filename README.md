# 🪙 Gateway de Pagamentos: Pix para Criptomoedas

[![Status do Projeto](https://img.shields.io/badge/Status-Em%20Produção-success.svg)](#)
[![Python FastAPI](https://img.shields.io/badge/Backend-FastAPI_Python-3776AB?logo=python&logoColor=white)](#)
[![Docker](https://img.shields.io/badge/Infraestrutura-Docker-2496ED?logo=docker&logoColor=white)](#)
[![Oracle Cloud](https://img.shields.io/badge/Cloud-Oracle_OCI-F80000?logo=oracle&logoColor=white)](#)

> 🚀 **Demo Online:** https://pix.solucoes-pagamento.com.br

## 📌 Sobre o Projeto
Este projeto é uma prova de conceito (PoC) de um Gateway de Pagamentos que simula a compra de criptomoedas através de transferências via Pix. 

O objetivo principal foi demonstrar a capacidade de integrar o sistema financeiro tradicional com cotações de cripto em tempo real, construindo uma arquitetura moderna, em contêineres e hospedada na nuvem.

## ⚙️ Arquitetura e Tecnologias
O projeto foi desenhado com foco em performance e facilidade de deploy:

* **Backend (API):** Python com **FastAPI** (alta performance e documentação Swagger automática).
* **Banco de Dados:** SQLite e SQLAlchemy ORM.
* **Integração Externa:** Consumo em tempo real da API pública da **Binance** para cotações.
* **Frontend:** HTML/CSS/JS focado na experiência do usuário (UX), com geração de QR Code dinâmico.
* **DevOps & Infraestrutura:** Orquestração com **Docker**, Proxy com **Nginx**, hospedagem na **Oracle Cloud (OCI)** e segurança **Cloudflare**.

## 💻 Como rodar o projeto localmente

1. Clone o repositório:
git clone https://github.com/Jefferson-Robson/pix-to-crypto-demo.git

2. Acesse a pasta:
cd pix-to-crypto-demo

3. Suba os contêineres utilizando Docker Compose:
docker-compose up -d --build

4. Acesse no navegador: http://localhost

---
*Desenvolvido por Jefferson Robson.*
