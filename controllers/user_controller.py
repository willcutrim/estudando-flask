from flask import request, jsonify
from flask.views import MethodView
from werkzeug.exceptions import BadRequest
from services.user_service import list_users, create_user


class AllUsers(MethodView):
    def get(self):
        users = list_users()
        return users


class CreateUser(MethodView):
    def post(self):
        try:
            user_data = request.get_json()
            if not user_data:
                raise BadRequest("Nenhum dado fornecido")
            
            new_user = create_user(user_data)
            return jsonify(new_user), 201
        except BadRequest as e:
            return jsonify({"error": str(e)}), 400
        except Exception as e:
            return jsonify({"error": "Erro interno do servidor"}), 500