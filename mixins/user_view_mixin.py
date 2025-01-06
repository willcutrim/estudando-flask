from flask.views import MethodView
from werkzeug.exceptions import BadRequest
from flask import request
from services.user_service import UserService


class JsonViewMixin(MethodView):
    def __init__(self):
        self.user_service = UserService()

    def post(self):
        if not request.is_json:
            raise BadRequest("Content-Type deve ser application/json")

        user_data = request.get_json()
        if not user_data:
            raise BadRequest("Nenhum dado fornecido")
        return user_data
