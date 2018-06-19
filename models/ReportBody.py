from models.ReportPart import ReportPart


class ReportBody(ReportPart):
    def __init__(self, report_type="body", content=""):
        super().__init__(report_type, content)
