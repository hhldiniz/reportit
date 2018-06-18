from utils.DBController import DBController


class ReportPart:
    def __init__(self, content="", user=None):
        self.__content = content
        self.__user = user

    def get_content(self):
        return self.__content

    def set_content(self, content):
        self.__content = content

    def set_user(self, user):
        self.__user = user

    def get_user(self):
        return self.__user

    def save(self):
        db_controller = DBController()
        insert_result = db_controller.insert("reports", {"content": self.get_content()})
        if insert_result is not None:
            return insert_result.inserted_id
        else:
            return None
