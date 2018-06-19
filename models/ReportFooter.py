from models.ReportPart import ReportPart


class ReportFooter(ReportPart):
    def __init__(self, report_type="footer", content=""):
        super().__init__(report_type, content)
