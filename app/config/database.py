# Importações necessárias do SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Permite carregar variáveis do arquivo .env
from dotenv import load_dotenv

import os

# Carrega as variáveis do arquivo .env para o ambiente
load_dotenv()

# Obtém a string de conexão com o banco a partir do .env
DATABASE_URL = os.getenv("DATABASE_URL")

# Cria o "motor" de conexão com o PostgreSQL
# É ele que estabelece a comunicação com o banco
engine = create_engine(DATABASE_URL)

# Cria uma fábrica de sessões
# Toda operação no banco (insert, update, delete, select)
# será feita através de uma sessão criada aqui
SessionLocal = sessionmaker(bind=engine)

# Classe base que todos os models devem herdar
# É ela que registra as tabelas no SQLAlchemy
Base = declarative_base()
