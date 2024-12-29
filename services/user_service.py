from werkzeug.exceptions import BadRequest

from messages.choices_messages import CAMPOS_OBRIGATORIOS, EMAIL_INVALIDO, EMAIL_DUPLICADO
from models.user import User
from utils.validations import email_duplicate, validate_email

DB = []

def list_users():
    return DB

def create_user(data):
    if 'name' not in data or 'email' not in data:
        raise BadRequest(CAMPOS_OBRIGATORIOS)
    
    if validate_email(data['email']):
        raise BadRequest(EMAIL_INVALIDO)
    
    if email_duplicate(data['email'], DB):
        raise BadRequest(EMAIL_DUPLICADO)
    
    new_user = User(id=len(DB) + 1, name=data['name'], email=data['email'])
    DB.append(new_user)
    return new_user

def get_user(user_id):
    return next((user for user in DB if user.id == user_id), None)

def update_user(user_id, data):
    user = get_user(user_id)
    if not user:
        return None
    
    if 'name' in data:
        user.name = data['name']
    
    if 'email' in data:
        if validate_email(data['email']):
            raise BadRequest(EMAIL_INVALIDO)
        
        if email_duplicate(data['email'], DB):
            raise BadRequest(EMAIL_DUPLICADO)
        
        user.email = data['email']
    
    return user

def delete_user(user_id):
    user = get_user(user_id)
    if not user:
        return None

    DB.remove(user)
    return user