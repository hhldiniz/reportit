from models.ReportPart import ReportPart


class ReportHeader(ReportPart):
    def __init__(self, report_type="header", content=""):
        super().__init__(report_type, content)
