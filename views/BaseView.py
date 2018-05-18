from flask import request, render_template
from flask.views import View


class BaseView(View):
    def __init__(self, template_name):
        self.__template_name = template_name

    def dispatch_request(self):
        if request.method == "GET":
            return self.get()
        elif request.method == "POST":
            return self.post()

    def get(self, **context):
        return render_template(self.__template_name, **context)

    def post(self, **context):
        return render_template(self.__template_name, **context)
