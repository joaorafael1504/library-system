# 📚 Library System API

API REST desenvolvida para gerenciamento de livros e autores em uma biblioteca.

---

## 📌 Descrição

Este projeto consiste em uma API construída em **Python com Flask**, permitindo realizar operações de CRUD (Create, Read, Update e Delete) sobre as entidades de autores e livros.

A aplicação utiliza banco de dados relacional **PostgreSQL** e implementa boas práticas de desenvolvimento backend, incluindo validação de dados e padronização de respostas através de DTOs.

---

## 🧱 Entidades

O sistema possui duas entidades principais:

- **Autor**
- **Livro**

### Relação entre entidades

- Um autor pode possuir vários livros  
- Um livro pertence a um único autor  

---

## ⚙️ Funcionalidades

### 👤 Autores
- Criar autor  
- Listar autores  
- Buscar autor por ID  
- Atualizar autor  
- Deletar autor  
  - Opção de remover livros associados  

---

### 📖 Livros
- Criar livro vinculado a um autor  
- Listar livros com dados do autor  
- Buscar livro por ID  
- Atualizar informações do livro  
- Deletar livro  

---

## 🛠️ Tecnologias Utilizadas

- **Python**
- **Flask**
- **PostgreSQL**
- **SQLAlchemy**
- **Marshmallow (DTOs para validação e serialização)**
- **Postman**
- **Git & GitHub**

---

## 🚀 Melhorias Futuras

- Implementação de autenticação (JWT)
- Documentação automática com Swagger/OpenAPI
- Deploy em ambiente de produção
- Testes automatizados

---

## 👨‍💻 Autor

Desenvolvido por **João Rafael**

---

## 📄 Licença

Este projeto está licenciado sob a **MIT License**.