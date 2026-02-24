# Importa tipos de coluna e chave estrangeira
from sqlalchemy import Boolean, Column, Integer, String, ForeignKey

# Permite criar relacionamento entre tabelas
from sqlalchemy.orm import relationship

# Importa Base para registrar a tabela
from app.config.database import Base

class Book(Base):
    __tablename__ = "books"  # Nome da tabela no banco

    # Chave primária do livro
    id = Column(Integer, primary_key=True)

    # Título do livro (campo obrigatório)
    title = Column(String(255), nullable=False)

    # Ano de publicação
    published_year = Column(Integer, nullable=False)

    # Indica se o livro está disponível para empréstimo
    available = Column(Boolean, default=True)

    # Chave estrangeira apontando para a tabela authors
    author_id = Column(Integer, ForeignKey("authors.id"), nullable=False)

    # Relacionamento ORM (não cria coluna nova)
    # Permite acessar book.author
    author = relationship("Author", back_populates="books")