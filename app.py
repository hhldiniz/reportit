from flask import Flask

from views.IndexView import IndexView

app = Flask(__name__)
# http://mysafeinfo.com/api/data?list=moviesbyearnings2010&format=html&alias=yr=year,rank=rank,tit=tittle,grs=gross,opn=opened,cnt=theatres

index_view = IndexView(template_name="index.html")
app.add_url_rule("/", view_func=index_view.as_view("index", template_name=index_view.get_template_name()))

if __name__ == '__main__':
    app.run()
