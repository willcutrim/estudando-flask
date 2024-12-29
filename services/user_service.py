from werkzeug.exceptions import BadRequest
from models.user import User
from utils.validations import email_duplicate, validate_email

DB = []

def list_users():
    if not DB:
        return []
    
    return DB

def create_user(data):
    if 'name' not in data or 'email' not in data:
        raise BadRequest("Os campos 'name' e 'email' são obrigatórios")
    
    if validate_email(data['email']):
        raise BadRequest("O campo 'email' é inválido")
    
    if email_duplicate(data['email'], DB):
        raise BadRequest("O email já está cadastrado")
    
    new_user = User(id=len(DB) + 1, name=data['name'], email=data['email'])
    DB.append(new_user)
    return new_user

def get_user(user_id):
    user = next((user for user in DB if user.id == user_id), None)
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
        
        if email_duplicate(data['email'], DB):
            raise BadRequest("O email já está cadastrado")
        
        user.email = data['email']
    
    return user

def delete_user(user_id):
    user = get_user(user_id)
    if not user:
        return None

    DB.remove(user)
    return user