from werkzeug.exceptions import BadRequest
from flask import request, jsonify

from messages.choices_messages import ERRO_INTERNO
from mixins.user_view_mixin import UserViewMixin


class AllUsersView(UserViewMixin):
    def get(self):
        users = self.user_service.list_users()
        return jsonify(users), 200 if users else 204


class CreateUserView(UserViewMixin):
    def post(self):
        user_data = super().post()
        new_user = self.user_service.create_user(user_data)
        return jsonify(new_user.to_dict()), 201


class GetUserView(UserViewMixin):
    def get(self, user_id):
        user = self.user_service.get_user(user_id)
        return jsonify(user.to_dict()), 200


class UpdateUserView(UserViewMixin):
    def put(self, user_id):
        user_data = request.get_json()
        updated_user = self.user_service.update_user(user_id, user_data)
        return jsonify(updated_user.to_dict()), 200


class DeleteUserView(UserViewMixin):
    def delete(self, user_id):
        self.user_service.delete_user(user_id)
        return jsonify({"message": "Usuário deletado"}), 200


class TestDbView(UserViewMixin):
    def get(self):
        result = self.user_service.test_db()
        return jsonify({"message": result}), 200


class ReativarUserView(UserViewMixin):
    def put(self, user_id):
        user = self.user_service.reativar_user(user_id)
        return jsonify({
            "message": "Usuário reativado com sucesso",
            "user": user.to_dict()
        }), 200