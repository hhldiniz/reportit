from utils.DBController import DBController


class ReportPart:
    def __init__(self, report_type, content="", user=None):
        self.__content = content
        self.__user = user
        self.__collection = "reports"
        self.__report_type = report_type

    def set_type(self, report_type):
        self.__report_type = report_type

    def get_type(self):
        return self.__report_type

    def get_content(self):
        return self.__content

    def set_content(self, content):
        self.__content = content

    def set_user(self, user):
        self.__user = user

    def get_user(self):
        return self.__user

    def set_collection(self, collection):
        self.__collection = collection

    def get_collection(self):
        return self.__collection

    @staticmethod
    def get():
        result = []
        db_controller = DBController()
        db_controller.connect()
        result.append(db_controller.as_array("report_header"))
        result.append(db_controller.as_array("report_body"))
        result.append(db_controller.as_array("report_footer"))
        return result

    def save(self):
        db_controller = DBController()
        db_controller.connect()
        insert_result = db_controller.insert(self.get_collection(), {
            "content": self.get_content(),
            "type": self.get_type()
        })
        if insert_result is not None:
            return insert_result.inserted_id
        else:
            return None
