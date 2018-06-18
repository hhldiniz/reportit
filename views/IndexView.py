from flask import session, request, redirect
import json
from models.User import User
from views.BaseView import BaseView
from utils.JSONEncoderUtil import JSONEncoderUtil


class IndexView(BaseView):
    def __init__(self, template_name):
        super().__init__(template_name)
        self.set_title("Home")

    def get(self, **context):
        try:
            context.__setitem__("user", json.loads(session["user"]))
        except KeyError:
            context.__setitem__("user", None)
        return super().get(**context)

    def post(self, **context):
        username = request.form["username"]
        password = request.form["password"]
        try:
            user = User.get({"username": username, "password": password})[0]
            if user.__len__() > 0:
                context.__setitem__("user", user)
                context.__setitem__("msg", None)
                session.__setitem__("user", JSONEncoderUtil().encode(user))
            else:
                context.__setitem__("msg", "Usuário ou senha incorretos!")
            return super().post(**context)
        except IndexError:
            return redirect("/error/login")

    @staticmethod
    def logout():
        session.__delitem__("user")
        return redirect("/")
