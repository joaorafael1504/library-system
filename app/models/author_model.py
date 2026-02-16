# Importa os tipos de coluna do SQLAlchemy
from sqlalchemy import Column, Integer, String

# Importa a classe Base para registrar a tabela
from app.config.database import Base

# Representa a tabela "authors" no banco de dados
class Author(Base):

    # Define o nome real da tabela no PostgreSQL
    __tablename__ = "authors"

    # Coluna id (chave primária, auto incremento)
    id = Column(Integer, primary_key=True, index=True)

    # Nome do autor (campo obrigatório)
    # nullable=False significa que não pode ser nulo
    name = Column(String, nullable=False)
