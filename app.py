from flask import Flask

app = Flask(__name__)
# http://mysafeinfo.com/api/data?list=moviesbyearnings2010&format=html&alias=yr=year,rank=rank,tit=tittle,grs=gross,opn=opened,cnt=theatres


if __name__ == '__main__':
    app.run()
