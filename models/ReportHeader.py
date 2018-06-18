from models.ReportPart import ReportPart


class ReportHeader(ReportPart):
    def __init__(self, content=""):
        super().__init__(content)
