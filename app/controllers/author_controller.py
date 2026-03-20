from flask import Blueprint, request, jsonify
from app import service
from app.config.database import SessionLocal
from app.service.author_service import AuthorService
from app.schemas.author_schema import (
    AuthorCreateDTO,
    AuthorUpdateDTO,
    AuthorResponseDTO
)

author_create_schema = AuthorCreateDTO()
author_update_schema = AuthorUpdateDTO()
author_response_schema = AuthorResponseDTO()
authors_response_schema = AuthorResponseDTO(many=True)

author_blueprint = Blueprint("author", __name__)

# Endpoint para criar autor
@author_blueprint.route("/authors", methods=["POST"])
def create_author():

    db = SessionLocal()  # cria sessão
    service = AuthorService(db)  # passa sessão

    data = author_create_schema.load(request.get_json())

    author = service.create_author(data["name"])

    result = author_response_schema.dump(author)

    return jsonify(result), 201

# Endpoint para listar autores
@author_blueprint.route("/authors", methods=["GET"])
def list_authors():

    db = SessionLocal()
    service = AuthorService(db)

    authors = service.list_authors()

    result = authors_response_schema.dump(authors)
    return jsonify(result)

# Endpoint para obter autor por ID
@author_blueprint.route("/authors/<int:author_id>", methods=["GET"])
def get_author(author_id):

    db = SessionLocal()
    service = AuthorService(db)

    try:
        author = service.get_author_by_id(author_id)

        return jsonify({
            "id": author.id,
            "name": author.name
        })

    except ValueError as e:
        return jsonify({"error": str(e)}), 404


# Endpoint para atualizar autor
@author_blueprint.route("/authors/<int:author_id>", methods=["PUT"])
def update_author(author_id):

    db = SessionLocal()
    service = AuthorService(db)

    data = author_update_schema.load(request.get_json())

    author = service.update_author(author_id, data["name"])

    result = author_response_schema.dump(author)

    return jsonify(result)

# Endpoint para deletar autor
@author_blueprint.route("/authors/<int:author_id>", methods=["DELETE"])
def delete_author(author_id):
    # Parâmetro opcional para deletar livros associados ao autor
    delete_books = request.args.get("delete_books", "false").lower() == "true"

    db = SessionLocal()
    service = AuthorService(db)

    try:
        service.delete_author(author_id, delete_books=delete_books)
        return jsonify({"message": "Author deleted successfully"})

    except ValueError as e:
        return jsonify({"error": str(e)}), 404