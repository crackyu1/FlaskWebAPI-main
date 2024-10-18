from http.client import HTTPException
from .myRequests import *
from flask import Flask, jsonify

def create_app():
    app = Flask(__name__,template_folder='./templates')
    
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
        elif isinstance(e, WeatherRequestError):
            return jsonify({
                "code": 400,
                "name": "Weather Request Error",
                "description": str(e),
            }), 400
        # 对于非 HTTP 异常，返回自定义的错误信息
        return jsonify({
            "code": 500,
            "name": "未知错误，联系对应开发人员",
            "description": str(e),
        }), 500
    @app.errorhandler(404)
    def page_not_found(e):
        return jsonify({
            "code": 404,
            "name": "Not Found",
            "description": "The requested URL was not found on the server.",
        }), 404
    return app
