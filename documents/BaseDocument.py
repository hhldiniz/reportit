import pdfkit


class BaseDocument:
    def __init__(self):
        self.__layout_path = None
        self.__output_path = "./"

    def set_layout_path(self, layout_path):
        self.__layout_path = layout_path

    def get_layout_path(self):
        return self.__layout_path

    def get_output_path(self):
        return self.__output_path

    def set_output_path(self, path):
        self.__output_path = path

    def generate_pdf(self, file_name):
        pdfkit.from_string(self.get_layout_path(), self.get_output_path()+file_name)

    def generate_csv(self, delimiter, quote_char, file_name):
        pass
