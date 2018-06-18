from views.BaseView import BaseView


class ErrorView(BaseView):
    def __init__(self, template_name):
        super().__init__(template_name)
        self.set_title("Erro")
        self.__msg = ""

    def get_msg(self):
        return self.__msg

    def set_msg(self, msg):
        self.__msg = msg
