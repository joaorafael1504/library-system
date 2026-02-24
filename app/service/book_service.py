from app.models.book_model import Book
from app.repositories.book_repository import BookRepository
from app.repositories.author_repository import AuthorRepository

class BookService:

    # Inicializa os repositories
    def __init__(self, db):
        self.book_repository = BookRepository(db)
        self.author_repository = AuthorRepository(db)

    # Cria um novo livro
    def create_book(self, title, published_year, author_id):

        # Verifica se o autor existe
        author = self.author_repository.get_by_id(author_id)
        if not author:
            raise Exception("Author not found")

        # Validação simples
        if not title:
            raise Exception("Title cannot be empty")

        # Cria objeto Book
        book = Book(
            title=title,
            published_year=published_year,
            author_id=author_id
        )

        # Salva no banco
        return self.book_repository.create(book)

    # Lista todos os livros
    def list_books(self):
        return self.book_repository.find_all()

    # Busca livro por id
    def get_book_by_id(self, book_id):
        book = self.book_repository.find_by_id(book_id)
        if not book:
            raise Exception("Book not found")
        return book

    # Remove livro
    def delete_book(self, book_id):
        book = self.book_repository.find_by_id(book_id)
        if not book:
            raise Exception("Book not found")
        # Deleta o livro usando o repository
        self.book_repository.delete(book)