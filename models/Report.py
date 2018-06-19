from utils.DBController import DBController


class Report:
    def __init__(self, content="", user=None):
        self.__content = content
        self.__user = user

    def set_content(self, content):
        self.__content = content

    def get_content(self):
        return self.__content

    def get_user(self):
        return self.__user

    def set_user(self, user):
        self.__user = user

    @staticmethod
    def get():
        db_controller = DBController()
        db_controller.connect()
        return db_controller.as_array("reports")

    def save(self):
        db_controller = DBController()
        db_controller.connect()
        insert_result = db_controller.insert("reports",
                                             {
                                                 "content": self.get_content(),
                                                 "user": self.get_content()
                                             })
        if insert_result is not None:
            return insert_result.inserted_id
        else:
            return None
