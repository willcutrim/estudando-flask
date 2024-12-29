from werkzeug.exceptions import BadRequest

from flask import request, jsonify
from flask.views import MethodView

from services.user_service import (
    list_users, create_user, get_user, update_user, delete_user
)


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


class GetUser(MethodView):
    def get(self, user_id):
        user = get_user(user_id)
        if not user:
            return jsonify({"error": "Usuário não encontrado"}), 404
        
        return jsonify(user.to_dict()), 200


class UpdateUser(MethodView):
    def put(self, user_id):
        try:
            user_data = request.get_json()
            if not user_data:
                raise BadRequest("Nenhum dado fornecido")
            
            user = update_user(user_id, user_data)

            if user is None:
                return jsonify({"error": "Usuário não encontrado"}), 404

            return jsonify(user.to_dict()), 200

        except BadRequest as e:
            return jsonify({"error": str(e)}), 400

        except Exception as e:
            return jsonify({"error": "Erro interno do servidor"}), 500
        

class DeleteUser(MethodView):
    def delete(self, user_id):
        try:
            user = delete_user(user_id)
            if user is None:
                return jsonify({"error": "Usuário não encontrado"}), 404
            
            return jsonify({'message': 'Usuário deletado'}), 200
        
        except Exception as e:
            return jsonify({"error": "Erro interno do servidor"}), 500
