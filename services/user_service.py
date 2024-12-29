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

def get_user(user_id):
    user = next((user for user in db if user.id == user_id), None)
    if not user:
        return None
    
    return user

def update_user(user_id, data):
    user = get_user(user_id)
    if not user:
        return None
    
    if 'name' in data:
        user.name = data['name']
    
    if 'email' in data:
        if validate_email(data['email']):
            raise BadRequest("O campo 'email' é inválido")
        
        user.email = data['email']
    
    return user