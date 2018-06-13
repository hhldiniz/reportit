from flask import Flask

from views.AboutView import AboutView
from views.IndexView import IndexView
from views.ReportsView import ReportsView

app = Flask(__name__)
# http://mysafeinfo.com/api/data?list=moviesbyearnings2010&format=html&alias=yr=year,rank=rank,tit=tittle,grs=gross,opn=opened,cnt=theatres

index_view = IndexView(template_name="index.html")
about_view = AboutView(template_name="about.html")
reports_view = ReportsView(template_name="reports.html")

app.add_url_rule("/", view_func=index_view.as_view("index", template_name=index_view.get_template_name()))
app.add_url_rule("/about", view_func=about_view.as_view("about", template_name=about_view.get_template_name()))
app.add_url_rule("/reports", view_func=reports_view.as_view("reports", template_name=reports_view.get_template_name()))

if __name__ == '__main__':
    app.run()
