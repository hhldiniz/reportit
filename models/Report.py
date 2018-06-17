from utils.DBController import DBController


class Report:
    def __init__(self, name="", header="", body="", footer="", user=None):
        self.__name = name
        self.__header = header
        self.__body = body
        self.__footer = footer
        self.__user = user

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_header(self, header):
        self.__header = header

    def get_header(self):
        return self.__header

    def set_body(self, body):
        self.__body = body

    def get_body(self):
        return self.__body

    def set_footer(self, footer):
        self.__footer = footer

    def get_user(self):
        return self.__user

    def set_user(self, user):
        self.__user = user

    def save(self):
        db_controller = DBController()
        insert_result = db_controller.insert("reports",
                                             {
                                                 "name": self.__name,
                                                 "header": self.__header,
                                                 "body": self.__body,
                                                 "footer": self.__footer,
                                                 "user": self.__user
                                             })
        if insert_result is not None:
            return insert_result.inserted_id
        else:
            return None
