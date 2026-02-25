from app.models.book_model import Book

class BookRepository:

    # Recebe a sessão do banco
    def __init__(self, db):
        self.db = db

    # Salva um novo livro
    def create(self, book):
        self.db.add(book)
        self.db.commit()
        self.db.refresh(book)  # Atualiza objeto com id gerado
        return book

    # Retorna todos os livros
    def find_all(self):
        return self.db.query(Book).all()

    # Busca livro pelo id
    def find_by_id(self, book_id):
        return self.db.query(Book).filter(Book.id == book_id).first()

    # Remove um livro
    def delete(self, book):
        self.db.delete(book)
        self.db.commit()

    # Atualiza um livro
    def update(self, book):
        self.db.commit()
        self.db.refresh(book)
        return book