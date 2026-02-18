from flask import Blueprint, request, jsonify
from app.service.author_service import AuthorService

# Blueprint é uma forma profissional de organizar rotas no Flask
author_blueprint = Blueprint("author", __name__)

service = AuthorService()

# Endpoint para criar autor
@author_blueprint.route("/authors", methods=["POST"])
def create_author():

    data = request.get_json()

    name = data.get("name")

    try:
        author = service.create_author(name)

        return jsonify({
            "id": author.id,
            "name": author.name
        }), 201

    except ValueError as e:
        return jsonify({"error": str(e)}), 400


# Endpoint para listar autores
@author_blueprint.route("/authors", methods=["GET"])
def list_authors():

    authors = service.list_authors()

    return jsonify([
        {
            "id": author.id,
            "name": author.name
        }
        for author in authors
    ])
