import pdfkit
from lxml import etree


class BaseDocument:
    def __init__(self):
        self.__layout_path = None
        self.__output_path = "../documents/outputs"
        self.__xml_path = None
        self.__xsl_path = None

    def set_output_path(self, path):
        self.__output_path = path

    def set_xml_path(self, xml_path):
        self.__xml_path = xml_path

    def set_xsl_path(self, xsl_path):
        self.__xsl_path = xsl_path

    def get_xml_path(self):
        return self.__xml_path

    def get_xsl_path(self):
        return self.__xsl_path

    def get_output_path(self):
        return self.__output_path

    def generate_pdf(self, file_name):
        pass

    def generate_csv(self, delimiter, quote_char, file_name):
        pass

    # Author: Siong-Ui Te
    # Modified
    def transform(self):
        # read xsl file
        xsl_root = etree.fromstring(open(self.__xsl_path).read().encode("ascii"))

        transform = etree.XSLT(xsl_root)

        # read xml
        xml_root = etree.fromstring(open(self.__xml_path).read().encode("ascii"))

        # transform xml with xslt
        trans_root = transform(xml_root)

        # return transformation result
        return etree.tostring(trans_root)

