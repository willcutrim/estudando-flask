from flask import make_response, jsonify
from werkzeug.exceptions import BadRequest
from models.user import User

db = []

def list_users():
    if not db:
        return make_response({'message': 'No users found'}, 204)
    
    return make_response(db, 200)

def create_user(data):
    if 'name' not in data or 'email' not in data:
        raise BadRequest("Os campos 'name' e 'email' são obrigatórios")
    
    new_user = User(id=len(db) + 1, name=data['name'], email=data['email'])
    db.append(new_user)
    return make_response(new_user, 201)