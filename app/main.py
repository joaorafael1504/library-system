from flask import Flask
from app.config.database import Base, engine

# Importa models (para registrar tabelas)
from app.models import author_model, book_model

# Importa blueprints
from app.controllers.author_controller import author_blueprint
from app.controllers.book_controller import book_blueprint

app = Flask(__name__)

# Cria todas as tabelas de uma vez
Base.metadata.create_all(bind=engine)

# Registra rotas
app.register_blueprint(author_blueprint)
app.register_blueprint(book_blueprint)

@app.route("/")
def home():
    return {"message": "Library API with Flask is running 🚀"}

if __name__ == "__main__":
    app.run(debug=True)