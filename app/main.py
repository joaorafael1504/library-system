# Importa o Flask para criar a aplicação web
from flask import Flask

# Importa o engine (conexão com o banco de dados)
from app.config.database import engine

# Importa os models para que o SQLAlchemy reconheça as tabelas
from app.models import author_model, book_model

# Cria a instância da aplicação Flask
app = Flask(__name__)

# Cria as tabelas no banco de dados caso ainda não existam
# O metadata contém todas as tabelas registradas na Base
# bind=engine informa qual conexão de banco será utilizada
author_model.Base.metadata.create_all(bind=engine)
book_model.Base.metadata.create_all(bind=engine)

# Rota simples apenas para testar se a API está funcionando
@app.route("/")
def home():
    return {"message": "Library API with Flask is running 🚀"}

# Executa a aplicação em modo de desenvolvimento
if __name__ == "__main__":
    app.run(debug=True)
