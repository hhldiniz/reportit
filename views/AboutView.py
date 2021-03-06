from views.BaseView import BaseView


class AboutView(BaseView):
    def __init__(self, template_name):
        super().__init__(template_name)

    def get(self, **context):
        context.__setitem__("title", "Sobre")
        return super().get(**context)
