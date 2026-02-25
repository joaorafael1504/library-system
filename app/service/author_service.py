from app.repositories.author_repository import AuthorRepository


class AuthorService:

    def __init__(self, db):
        self.db = db
        self.repository = AuthorRepository(db)

    def create_author(self, name):
        # Valida o nome do autor (não pode ser vazio)
        if not name:
            raise ValueError("Author name cannot be empty")

       # Verifica se já existe autor com mesmo nome
        existing_author = self.repository.get_by_name(name)
        if existing_author:
            raise ValueError("Author already exists")
        # Se passar nas validações, cria o autor
        return self.repository.create(name)

    def list_authors(self):
        # Retorna todos os autores cadastrados.
        return self.repository.get_all()

    def get_author_by_id(self, author_id):
        # Retorna um autor pelo ID ou lança um erro se não encontrado
        author = self.repository.get_by_id(author_id)
        # Se o autor não existir, lança um erro
        if not author:
            raise ValueError("Author not found")
        # Se existir, retorna o autor
        return author

    def update_author(self, author_id, name):
        # Verifica se o autor existe
        author = self.repository.get_by_id(author_id)

        if not author:
            raise ValueError("Author not found")

        # Validação de nome
        if not name or not name.strip():
            raise ValueError("Author name cannot be empty")

        # Verifica duplicidade (exceto ele mesmo)
        existing_author = self.repository.get_by_name(name)

        if existing_author and existing_author.id != author_id:
            raise ValueError("Author name already in use")

        # Atualiza o nome
        author.name = name
        # Salva as alterações no banco
        return self.repository.update(author)

    def delete_author(self, author_id, delete_books=False):
        # Verifica se o autor existe
        author = self.repository.get_by_id(author_id)
        # Se não existir, lança um erro
        if not author:
            raise ValueError("Author not found")
        
        # Se o autor tiver livros associados e delete_books for False, lança um erro
        if author.books and not delete_books:
            raise ValueError("Cannot delete author with existing books")

        if delete_books:
            # Se delete_books for True, deleta os livros associados ao autor
            for books in author.books:
                self.db.delete(books)
        # Se existir, deleta o autor
        self.repository.delete(author)
