class BaseDocument:
    def __init__(self, header, body, footer):
        self.__header = header
        self.__body = body
        self.__footer = footer

    def get_header(self):
        return self.__header

    def get_body(self):
        return self.__body

    def get_footer(self):
        return self.__footer

    def set_header(self, header):
        self.__header = header

    def set_body(self, body):
        self.__body = body

    def set_footer(self, footer):
        self.__footer = footer
