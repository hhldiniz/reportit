from views.BaseView import BaseView


class SignupView(BaseView):
    def __init__(self, template_name):
        super().__init__(template_name)

    def get(self, **context):
        context.__setitem__("title", "Cadastro")
        return super().get(**context)
