# 📚 API de Biblioteca (CRUD)

## 📌 Descrição do Projeto

Este projeto consiste no desenvolvimento de uma **API REST** para gerenciar livros de uma pequena biblioteca.

O sistema permite realizar operações básicas de **CRUD (Create, Read, Update, Delete)**.

A API será desenvolvida em **Python**, utilizando **PostgreSQL** como banco de dados, e os endpoints serão testados por meio do **Postman**.

---

## 🧱 Entidades do Sistema

O sistema irá possuir apenas duas entidades:

- **Autor**
- **Livro**

---

## 🔄 Funcionalidades CRUD

### Autores
- Criar autor  
- Listar autores  
- Atualizar autor  
- Deletar autor (opcionalmente, remover também todos os livros associados a esse autor)  

### Livros
- Criar livro (associando a um autor existente)  
- Listar livros (exibindo o nome do autor)  
- Atualizar informações do livro  
- Deletar livro  

---

## 🛠️ Tecnologias Utilizadas
- Python  
- API REST  
- PostgreSQL  
- Postman (para testes dos endpoints)  

---

## 🗄️ Banco de Dados

O banco de dados segue um relacionamento simples:

- Um autor pode possuir vários livros  
- Um livro pertence a um único autor  

---

## 👤 Autor

Desenvolvido por **João Rafael**.

---

## 📄 Licença

Este projeto está licenciado sob a **MIT License**.