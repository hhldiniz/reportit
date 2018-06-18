from flask import request, session
import json
from models.User import User
from views.BaseView import BaseView


class SignupView(BaseView):
    def __init__(self, template_name):
        super().__init__(template_name)

    def get(self, **context):
        context.__setitem__("title", "Cadastro")
        return super().get(**context)

    def post(self, **context):
        name = request.form["name"]
        email = request.form["email"]
        username = request.form["username"]
        password = request.form["password"]
        password_confirm = request.form["password_confirm"]
        user = User(name, email, username, password)
        if password == password_confirm:
            user.save()
            context.__setitem__("msg", "Cadastro realizado com sucesso!")
            session.__setitem__("user", json.dumps(user))
        else:
            context.__setitem__("msg", "Erro ao realizar o cadastro")
        return super().post(**context)
