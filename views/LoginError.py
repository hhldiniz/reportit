from views.ErrorView import ErrorView


class LoginError(ErrorView):
    def __init__(self, template_name):
        super().__init__(template_name)
        self.set_msg("Usuário ou senha incorretos")

    def get(self, **context):
        context.__setitem__("msg", self.get_msg())
        return super().get(**context)
