from app.models.author_model import Author
from app.config.database import SessionLocal

class AuthorRepository:

    def __init__(self):
        # Cria uma sessão com o banco de dados
        self.db = SessionLocal()

    def create(self, name):
        # Cria um objeto Author
        author = Author(name=name)

        # Adiciona à sessão
        self.db.add(author)

        # Salva no banco
        self.db.commit()

        # Atualiza o objeto com o id gerado
        self.db.refresh(author)

        return author

    def get_all(self):
        # Retorna todos os autores
        return self.db.query(Author).all()
