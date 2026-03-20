from marshmallow import Schema, fields, validate

# DTO responsável por validar os dados recebidos na criação de um autor.
# Garante que o nome seja obrigatório e tenha pelo menos 2 caracteres.
class AuthorCreateDTO(Schema):
    name = fields.Str(required=True, validate=validate.Length(min=2))

# DTO utilizado na atualização de um autor existente.
# Define quais campos podem ser alterados.
class AuthorUpdateDTO(Schema):
    name = fields.Str(required=True)

# DTO de saída que define quais dados do autor serão expostos na API.
# Evita retornar diretamente a entidade do banco.
class AuthorResponseDTO(Schema):
    id = fields.Int()
    name = fields.Str()