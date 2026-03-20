from flask import Blueprint, request, jsonify
from app.config.database import SessionLocal
from app.service.book_service import BookService
from app.schemas.book_schema import (
    BookCreateDTO,
    BookUpdateDTO,
    BookResponseDTO
)

book_create_schema = BookCreateDTO()
book_update_schema = BookUpdateDTO()
book_response_schema = BookResponseDTO()
books_response_schema = BookResponseDTO(many=True)

# Criação do blueprint
book_blueprint = Blueprint("book_controller", __name__)

# Endpoint para criar livro
@book_blueprint.route("/books", methods=["POST"])
def create_book():
    db = SessionLocal()
    service = BookService(db)

    data = book_create_schema.load(request.get_json())

    book = service.create_book(
        data["title"],
        data["published_year"],
        data["author_id"]
    )

    result = book_response_schema.dump(book)

    return jsonify(result), 201

# Endpoint para listar todos os livros
@book_blueprint.route("/books", methods=["GET"])
def list_books():
    db = SessionLocal()
    service = BookService(db)

    books = service.list_books()

    result = books_response_schema.dump(books)
    return jsonify(result)

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
            "author_id": book.author_id,
            "author_name": book.author_name
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

# Endpoint para atualizar livro
@book_blueprint.route("/books/<int:book_id>", methods=["PUT"])
def update_book(book_id):

    db = SessionLocal()
    service = BookService(db)

    data = book_update_schema.load(request.get_json())

    book = service.update_book(
        book_id,
        data.get("title"),
        data.get("published_year"),
        data.get("author_id"),
        data.get("available")
    )

    result = book_response_schema.dump(book)

    return jsonify(result)
