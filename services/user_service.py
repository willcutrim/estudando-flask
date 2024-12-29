from flask import make_response, jsonify
from werkzeug.exceptions import BadRequest
from models.user import User
from utils.validations import validate_email

db = []

def list_users():
    if not db:
        return []
    
    return db

def create_user(data):
    if 'name' not in data or 'email' not in data:
        raise BadRequest("Os campos 'name' e 'email' são obrigatórios")
    
    if validate_email(data['email']):
        raise BadRequest("O campo 'email' é inválido")
    
    new_user = User(id=len(db) + 1, name=data['name'], email=data['email'])
    db.append(new_user)
    return new_user