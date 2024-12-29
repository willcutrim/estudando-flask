from werkzeug.exceptions import BadRequest

from flask import request, jsonify
from flask.views import MethodView

from services.user_service import list_users, create_user


class AllUsers(MethodView):
    def get(self):
        users = list_users()
        return jsonify([user.to_dict() for user in users]), 200 if users else 204


class CreateUser(MethodView):
    def post(self):
        try:
            user_data = request.get_json()
            if not user_data:
                raise BadRequest("Nenhum dado fornecido")
            
            new_user = create_user(user_data)
            return jsonify(new_user.to_dict()), 201

        except BadRequest as e:
            return jsonify({"error": str(e)}), 400

        except Exception as e:
            return jsonify({"error": "Erro interno do servidor"}), 500