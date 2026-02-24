from flask import Blueprint, request, jsonify
from app.config.database import SessionLocal
from app.service.book_service import BookService

# Criação do blueprint
book_blueprint = Blueprint("book_controller", __name__)

# Endpoint para criar livro
@book_blueprint.route("/books", methods=["POST"])
def create_book():
    db = SessionLocal()
    service = BookService(db)

    data = request.get_json()

    try:
        book = service.create_book(
            data["title"],
            data["published_year"],
            data["author_id"]
        )

        return jsonify({
            "id": book.id,
            "title": book.title,
            "published_year": book.published_year,
            "available": book.available,
            "author_id": book.author_id
        }), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 400


# Endpoint para listar todos os livros
@book_blueprint.route("/books", methods=["GET"])
def list_books():
    db = SessionLocal()
    service = BookService(db)

    books = service.list_books()

    return jsonify([
        {
            "id": b.id,
            "title": b.title,
            "published_year": b.published_year,
            "available": b.available,
            "author_id": b.author_id
        }
        for b in books
    ])


# Endpoint para buscar livro por id
@book_blueprint.route("/books/<int:book_id>", methods=["GET"])
def get_book(book_id):
    db = SessionLocal()
    service = BookService(db)

    try:
        book = service.get_book_by_id(book_id)

        return jsonify({
            "id": book.id,
            "title": book.title,
            "published_year": book.published_year,
            "available": book.available,
            "author_id": book.author_id
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 404


# Endpoint para deletar livro
@book_blueprint.route("/books/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    db = SessionLocal()
    service = BookService(db)

    try:
        service.delete_book(book_id)
        return jsonify({"message": "Book deleted successfully"})

    except Exception as e:
        return jsonify({"error": str(e)}), 404