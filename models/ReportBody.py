from models.ReportPart import ReportPart


class ReportBody(ReportPart):
    def __init__(self, content=""):
        super().__init__(content)
