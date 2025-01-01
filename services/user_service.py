from datetime import datetime
from werkzeug.exceptions import BadRequest

from messages.choices_messages import CAMPOS_OBRIGATORIOS, EMAIL_INVALIDO, EMAIL_DUPLICADO
from models.user import User
from utils.validations import email_duplicate, validate_email
from config.database import db
from sqlalchemy.sql import text

def list_users():
    try:
        users = User.query.all()
        return users
    except Exception as e:
        raise BadRequest(f"Erro ao listar usuários: {e}")

def create_user(data):
    try:
        if 'username' not in data or 'email' not in data:
            raise BadRequest(CAMPOS_OBRIGATORIOS)
        
        if validate_email(data['email']):
            raise BadRequest(EMAIL_INVALIDO)
        
        if email_duplicate(data['email'], User.query.all()):
            raise BadRequest(EMAIL_DUPLICADO)
        
        new_user = User(username=data['username'], email=data['email'], created_at=datetime.now())
        db.session.add(new_user)
        db.session.commit()
        return new_user
    except Exception as e:
        raise BadRequest(f"Erro ao criar usuário: {e}")

def get_user(user_id):
    try:
        user = User.query.get(user_id)
        if not user:
            raise BadRequest("Usuário não encontrado")
        return user
    
    except Exception as e:
        raise BadRequest(f"Erro ao obter usuário: {e}")

def update_user(user_id, data):
    try:
        user = User.query.get(user_id)
        if not user:
            raise BadRequest("Usuário não encontrado")
        
        if 'username' in data:
            user.username = data['username']

        if 'email' in data:
            if validate_email(data['email']):
                raise BadRequest(EMAIL_INVALIDO)
            
            if email_duplicate(data['email'], User.query.all()):
                raise BadRequest(EMAIL_DUPLICADO)
            
            user.email = data['email']
        
        db.session.commit()
        return user
    
    except Exception as e:
        raise BadRequest(f"Erro ao atualizar usuário: {e}")

def delete_user(user_id):
    try:
        user = User.query.get(user_id)
        if not user:
            raise BadRequest("Usuário não encontrado")
        
        user.is_active = False
        db.session.commit()

    except Exception as e:
        raise BadRequest(f"Erro ao deletar usuário: {e}")

def test_db():
    try:
        with db.engine.connect() as connection:
            connection.execute(text('SELECT 1'))
        return "Conexão com o banco de dados funcionando!"
    except Exception as e:
        return f"Erro ao conectar ao banco de dados: {e}"

def reativar_user(user_id):
    try:
        user = get_user(user_id)
        
        user.is_active = True
        db.session.commit()
        return user
    
    except Exception as e:
        raise BadRequest(f"Erro ao reativar usuário: {e}")
