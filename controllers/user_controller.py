from werkzeug.exceptions import BadRequest

from flask import request, jsonify
from flask.views import MethodView

from messages.choices_messages import ERRO_INTERNO
from services.user_service import (
    list_users, create_user, get_user, test_db, update_user, delete_user,
    reativar_user
)


class AllUsers(MethodView):
    def get(self):
        users = list_users()
        return jsonify(users), 200 if users else 204


class CreateUser(MethodView):
    def post(self):
        user_data = request.get_json()
        if not user_data:
            raise BadRequest("Nenhum dado fornecido")
        
        new_user = create_user(user_data)
        return jsonify(new_user.to_dict()), 201


class GetUser(MethodView):
    def get(self, user_id):
        user = get_user(user_id)
        return jsonify(user.to_dict()), 200


class UpdateUser(MethodView):
    def put(self, user_id):
        user_data = request.get_json()
        updated_user = update_user(user_id, user_data)
        return jsonify(updated_user.to_dict()), 200


class DeleteUser(MethodView):
    def delete(self, user_id):
        delete_user(user_id)
        return jsonify({"message": "Usuário deletado"}), 200


class TestDb(MethodView):
    def get(self):
        result = test_db()
        return jsonify({"message": result}), 200
    
class ReativarUser(MethodView):
    def put(self, user_id):
        user = reativar_user(user_id)
        return jsonify({
            "message": "Usuário reativado com sucesso",
            "user": user.to_dict()
        }), 200