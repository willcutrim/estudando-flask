from werkzeug.exceptions import BadRequest

from flask import request, jsonify
from flask.views import MethodView

from messages.choices_messages import ERRO_INTERNO
from services.user_service import UserService


class AllUsersView(MethodView):
    def __init__(self):
        self.user_service = UserService()
        super().__init__()

    def get(self):
        users = self.user_service.list_users()
        return jsonify(users), 200 if users else 204


class CreateUserView(MethodView):
    def __init__(self):
        self.user_service = UserService()
        super().__init__()

    def post(self):
        user_data = request.get_json()
        if not user_data:
            raise BadRequest("Nenhum dado fornecido")
        
        new_user = self.user_service.create_user(user_data)
        return jsonify(new_user.to_dict()), 201


class GetUserView(MethodView):
    def __init__(self):
        self.user_service = UserService()
        super().__init__()

    def get(self, user_id):
        user = self.user_service.get_user(user_id)
        return jsonify(user.to_dict()), 200


class UpdateUserView(MethodView):
    def __init__(self):
        self.user_service = UserService()
        super().__init__()

    def put(self, user_id):
        user_data = request.get_json()
        updated_user = self.user_service.update_user(user_id, user_data)
        return jsonify(updated_user.to_dict()), 200


class DeleteUserView(MethodView):
    def __init__(self):
        self.user_service = UserService()
        super().__init__()

    def delete(self, user_id):
        self.user_service.delete_user(user_id)
        return jsonify({"message": "Usuário deletado"}), 200


class TestDbView(MethodView):
    def __init__(self):
        self.user_service = UserService()
        super().__init__()

    def get(self):
        result = self.user_service.test_db()
        return jsonify({"message": result}), 200


class ReativarUserView(MethodView):
    def __init__(self):
        self.user_service = UserService()
        super().__init__()

    def put(self, user_id):
        user = self.user_service.reativar_user(user_id)
        return jsonify({
            "message": "Usuário reativado com sucesso",
            "user": user.to_dict()
        }), 200