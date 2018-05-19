from flask import request, render_template
from flask.views import View


class BaseView(View):
    def __init__(self, template_name):
        self.__template_name = template_name
        self.__title = "Title"

    def set_title(self, title):
        self.__title = title

    def get_title(self):
        return self.__title

    def dispatch_request(self):
        if request.method == "GET":
            return self.get(title=self.get_title())
        elif request.method == "POST":
            return self.post(title=self.get_title())

    def get(self, **context):
        return render_template(self.__template_name, **context)

    def post(self, **context):
        return render_template(self.__template_name, **context)

    def get_template_name(self):
        return self.__template_name