import json

from flask import request, session

from models.Report import Report
from models.ReportPart import ReportPart
from views.BaseView import BaseView


class ReportsView(BaseView):
    def __init__(self, template_name):
        super().__init__(template_name)

    def get(self, **context):
        context.__setitem__("title", "Relatórios")
        report_parts = ReportPart.get()
        reports = Report.get()
        context.__setitem__("report_parts", report_parts)
        context.__setitem__("reports", reports)
        return super().get(**context)

    def post(self, **context):
        report_type_selection = request.form["report_type_selection"]
        report_input = request.form["report_input"]
        report = None
        if report_type_selection != '':
            if report_type_selection == "1":
                from models.ReportHeader import ReportHeader
                report = ReportHeader()
                report.set_collection("report_header")
            elif report_type_selection == "2":
                from models.ReportBody import ReportBody
                report = ReportBody()
                report.set_collection("report_body")
            elif report_type_selection == "3":
                from models.ReportFooter import ReportFooter
                report = ReportFooter()
                report.set_collection("report_footer")
        else:
            from models.Report import Report
            report = Report()
        report.set_user(session["user"])
        report.set_content(report_input)
        if report.save() is not None:
            return json.dumps({"result": True})
        else:
            return json.dumps({"result": False})
