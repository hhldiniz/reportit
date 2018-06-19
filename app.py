from flask import Flask

from views.AboutView import AboutView
from views.IndexView import IndexView
from views.LoginError import LoginError
from views.ReportsView import ReportsView
from views.SignupView import SignupView

app = Flask(__name__)
app.secret_key = "E7162800D84BFB861148F6F8E17462697866C542FE2E0E7D87AF0D01E209AB12"

index_view = IndexView(template_name="index.html")
about_view = AboutView(template_name="about.html")
reports_view = ReportsView(template_name="reports.html")
signup_view = SignupView(template_name="signup.html")
error_view = LoginError(template_name="login_error.html")

app.add_url_rule("/", methods=["GET", "POST"],
                 view_func=index_view.as_view("index", template_name=index_view.get_template_name()))
app.add_url_rule("/about", view_func=about_view.as_view("about", template_name=about_view.get_template_name()))
app.add_url_rule("/reports", methods=["GET","POST"], view_func=reports_view.as_view("reports", template_name=reports_view.get_template_name()))
app.add_url_rule("/signup", methods=["GET", "POST"],
                 view_func=signup_view.as_view("signup", template_name=signup_view.get_template_name()))
app.add_url_rule("/error/login", view_func=error_view.as_view("error_login", template_name=error_view.get_template_name()))


@app.route("/logout")
def logout():
    return index_view.logout()


if __name__ == '__main__':
    app.config["SESSION_TYPE"] = "mongodb"
    app.run()
