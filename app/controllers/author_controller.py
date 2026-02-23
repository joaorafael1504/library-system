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
# Se a criação for bem-sucedida, retorna os dados do autor criado com status 201
        return jsonify({
            "id": author.id,
            "name": author.name
        }), 201
# Em caso de erro de validação, retorna 400 com a mensagem de erro
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

# Endpoint para obter autor por ID
@author_blueprint.route("/authors/<int:author_id>", methods=["GET"])
def get_author(author_id):

    try:
        author = service.get_author_by_id(author_id)

        return jsonify({
            "id": author.id,
            "name": author.name
        })

    except ValueError as e:
        # Retorna 404 caso autor não exista
        return jsonify({"error": str(e)}), 404
    

# Endpoint para atualizar autor
@author_blueprint.route("/authors/<int:author_id>", methods=["PUT"])
def update_author(author_id):

    data = request.get_json()
    name = data.get("name")

    try:
        author = service.update_author(author_id, name)

        return jsonify({
            "id": author.id,
            "name": author.name
        })
# Em caso de erro de validação, retorna 400 ou 404 dependendo do tipo de erro
    except ValueError as e:

        # Autor não encontrado 
        if "not found" in str(e):
            return jsonify({"error": str(e)}), 404

        # Nome duplicado 
        if "already in use" in str(e):
            return jsonify({"error": str(e)}), 409

        # Outros erros de validação
        return jsonify({"error": str(e)}), 400

# Endpoint para deletar autor
@author_blueprint.route("/authors/<int:author_id>", methods=["DELETE"])
def delete_author(author_id):

    try:
        service.delete_author(author_id)
# Se a exclusão for bem-sucedida, retorna mensagem de sucesso
        return jsonify({"message": "Author deleted successfully"})
# Se o autor não for encontrado, retorna 404
    except ValueError as e:
        return jsonify({"error": str(e)}), 404