from flask import jsonify, render_template, request
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

@app.errorhandler(Exception)
def handle_exception(e):
    # 如果是 HTTP 异常，返回标准的错误描述和状态码
    if isinstance(e, HTTPException):
        response = e.get_response()
        response.data = jsonify({
            "code": e.code,
            "name": e.name,
            "description": e.description,
        }).data
        response.content_type = "application/json"
        return response
    # 对于非 HTTP 异常，返回自定义的错误信息
    return jsonify({
        "code": 400,
        "name": "paramError",
        "description": str(e),
    }), 400



if __name__=="__main__":
    app.run(debug=True,host='127.0.0.1', port=5000)