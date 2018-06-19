import json

from flask import request, session

from views.BaseView import BaseView


class ReportsView(BaseView):
    def __init__(self, template_name):
        super().__init__(template_name)

    def get(self, **context):
        context.__setitem__("title", "Relatórios")
        return super().get(**context)

    def post(self, **context):
        print(request.form)
        report_type_selection = request.form["report_type_selection"]
        report_input = request.form["report_input"]
        if report_type_selection is not None:
            if report_type_selection == "1":
                from models.ReportHeader import ReportHeader
                report = ReportHeader()
                report.set_collection("report_header")
            elif report_type_selection == "2":
                from models.ReportBody import ReportBody
                report = ReportBody()
                report.set_collection("report_body")
            else:
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
