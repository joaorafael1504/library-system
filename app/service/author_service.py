from app.repositories.author_repository import AuthorRepository

class AuthorService:

    def __init__(self):
        self.repository = AuthorRepository()

    def create_author(self, name):
        # Aqui é onde regras de negócio ficariam
        # Exemplo: validar tamanho do nome, impedir nome vazio etc.

        if not name:
            raise ValueError("Author name cannot be empty")

        return self.repository.create(name)

    def list_authors(self):
        return self.repository.get_all()
