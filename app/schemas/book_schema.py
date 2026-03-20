from marshmallow import Schema, fields

# DTO responsável por validar os dados de entrada na criação de um livro.
# Garante que todos os campos obrigatórios estejam presentes e corretos.
class BookCreateDTO(Schema):
    title = fields.Str(required=True)
    published_year = fields.Int(required=True)
    author_id = fields.Int(required=True)

# DTO utilizado para atualização de um livro.
# Permite atualização parcial dos campos (todos opcionais).
class BookUpdateDTO(Schema):
    title = fields.Str()
    published_year = fields.Int()
    author_id = fields.Int()
    available = fields.Bool()

# DTO auxiliar para representar os dados do autor dentro da resposta de livro.
# Evita expor a entidade completa e mantém o retorno mais controlado.
class AuthorNestedDTO(Schema):
    id = fields.Int()
    name = fields.Str()

# DTO de saída do livro.
# Define exatamente o formato da resposta da API, incluindo o autor associado.
class BookResponseDTO(Schema):
    id = fields.Int()
    title = fields.Str()
    published_year = fields.Int()
    available = fields.Bool()
    author = fields.Nested(AuthorNestedDTO)