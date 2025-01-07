from datetime import datetime
from werkzeug.exceptions import BadRequest

from messages.choices_messages import CAMPOS_OBRIGATORIOS, EMAIL_INVALIDO, EMAIL_DUPLICADO
from models.user import User, Address
from schema.schema import UserSchemaUser
from utils.validations import UserValidation
from config.database import db


class UserService:
    def __init__(self):
        self.validation = UserValidation()

    def list_users(self):
        try:
            users = User.query.all()
            schema_users = UserSchemaUser(many=True)
            return schema_users.dump(users)

        except Exception as e:
            raise BadRequest(f"Erro ao listar usuários: {e}")

    def create_user(self, data):
        try:
            if 'username' not in data or 'email' not in data:
                raise BadRequest(CAMPOS_OBRIGATORIOS)
            
            if self.validation.validate_email(data['email']):
                raise BadRequest(EMAIL_INVALIDO)
            
            if self.validation.email_duplicate(data['email'], User.query.all()):
                raise BadRequest(EMAIL_DUPLICADO)
            
            new_user = User(username=data['username'], email=data['email'], created_at=datetime.now())
            db.session.add(new_user)
            db.session.commit()

            if 'address' in data:
                address_data = data['address']
                new_address = Address(
                    user_id=new_user.id,
                    address=address_data['address'],
                    city=address_data['city'],
                    state=address_data['state'],
                    country=address_data['country']
                )
                db.session.add(new_address)
                db.session.commit()
  
            schema_new_user = UserSchemaUser()

            return schema_new_user.dump(new_user)

        except Exception as e:
            raise BadRequest(f"Erro ao criar usuário: {e}")

    def get_user(self, user_id):
        try:
            user = User.query.get(user_id)
            if not user:
                raise BadRequest("Usuário não encontrado")

            user_schema = UserSchemaUser(exclude=['address'])

            return user_schema.dump(user)
        
        except Exception as e:
            raise BadRequest(f"Erro ao obter usuário: {e}")

    def update_user(self, user_id, data):
        try:
            user = User.query.get(user_id)
            if not user:
                raise BadRequest("Usuário não encontrado")
            
            if 'username' in data:
                user.username = data['username']

            if 'email' in data:
                if self.validation.validate_email(data['email']):
                    raise BadRequest(EMAIL_INVALIDO)
                
                if self.validation.email_duplicate(data['email'], User.query.all()):
                    raise BadRequest(EMAIL_DUPLICADO)
                
                user.email = data['email']
            
            db.session.commit()

            schema_user_updated = UserSchemaUser()

            return schema_user_updated.dump(user)
        
        except Exception as e:
            raise BadRequest(f"Erro ao atualizar usuário: {e}")

    def delete_user(self, user_id):
        try:
            user = User.query.get(user_id)
            if not user:
                raise BadRequest("Usuário não encontrado")
            
            user.is_active = False
            db.session.commit()

        except Exception as e:
            raise BadRequest(f"Erro ao deletar usuário: {e}")

    def reativar_user(self, user_id):
        try:
            user = self.get_user(user_id)

            user['is_active'] = True
            db.session.commit()

            return user
        
        except Exception as e:
            raise BadRequest(f"Erro ao reativar usuário: {e}")
