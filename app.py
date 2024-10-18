from flask import abort, jsonify, render_template, request
from werkzeug.exceptions import HTTPException

from app import create_app
from app.myRequests import get

app = create_app()


@app.route("/<province>/<city>")

def getWeather(province,city):
    # province = request.args.get('province')
    # city = request.args.get('city')
    list=get(province=province,city=city)
    return render_template("result.html",place = list[0] ,temperature = list[1],weather = list[2])

@app.route("/")
def home():
    return render_template("home.html")



if __name__=="__main__":
    app.run(host='127.0.0.1', port=5000)