# Importa tipos de coluna e chave estrangeira
from sqlalchemy import Column, Integer, String, ForeignKey

# Permite criar relacionamento entre tabelas
from sqlalchemy.orm import relationship

# Importa Base para registrar a tabela
from app.config.database import Base

# Representa a tabela "books"
class Book(Base):

    # Nome da tabela no banco
    __tablename__ = "books"

    # Chave primária
    id = Column(Integer, primary_key=True, index=True)

    # Título do livro (obrigatório)
    title = Column(String, nullable=False)

    # Ano de publicação (opcional)
    publication_year = Column(Integer)

    # Chave estrangeira que aponta para authors.id
    # Isso cria o relacionamento no banco
    author_id = Column(Integer, ForeignKey("authors.id"))

    # Relacionamento no nível do Python
    # Permite acessar o autor assim:
    # book.author.name
    author = relationship("Author")