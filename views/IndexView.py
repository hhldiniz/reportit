from flask import session, request

from models.User import User
from views.BaseView import BaseView


class IndexView(BaseView):
    def __init__(self, template_name):
        super().__init__(template_name)
        self.set_title("Home")

    def get(self, **context):
        try:
            context.__setitem__("user", session["user"])
        except KeyError:
            context.__setitem__("user", None)
        return super().get(**context)

    def post(self, **context):
        username = request.form["username"]
        password = request.form["password"]
        user = User.get({"username": username, "password": password})
        if user.__len__() > 0:
            context.__setitem__("user", user)
            context.__setitem__("msg", None)
        else:
            context.__setitem__("msg", "Usuário ou senha incorretos!")
        return super().post(**context)

    def logout(self):
        session.__delitem__("user")
        self.get()
