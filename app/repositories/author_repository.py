from app.models.author_model import Author


class AuthorRepository:

    def __init__(self, db):
        # Recebe a sessão do banco
        self.db = db

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

    def get_by_name(self, name):
        # Retorna o autor com o nome especificado ou None se não existir
        return self.db.query(Author).filter(Author.name == name).first()

    def get_by_id(self, author_id):
        # Retorna o autor com o ID especificado ou None se não existir
        return self.db.query(Author).filter(Author.id == author_id).first()

    def update(self, author):
        # Atualiza o autor no banco
        self.db.commit()
        self.db.refresh(author)
        return author

    def delete(self, author):
        # Remove o autor do banco
        self.db.delete(author)
        self.db.commit()
