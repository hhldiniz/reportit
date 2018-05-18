from documents.BaseDocument import BaseDocument


class MoviesByEarning(BaseDocument):
    def __init__(self, data_source, data_type):
        super().__init__()
        self.__data_source = data_source
        self.__data_type = data_type
