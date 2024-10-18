from http.client import HTTPException
from .myRequests import *
from flask import Flask, jsonify

def create_app():
    app = Flask(__name__,template_folder='./templates')
    
    @app.errorhandler(Exception)
    def handle_exception(e):
        return jsonify({
            "code": 500,
            "name": "未知错误，联系对应开发人员",
            "description": str(e),
        }), 500
        
    @app.errorhandler(WeatherRequestError)
    def handle_exception(WeatherRequestError):
        return jsonify({
            "code": 400,
            "name": "Weather Request Error",
            "description": str(WeatherRequestError),
        }), 400
        # 对于非 HTTP 异常，返回自定义的错误信息

    @app.errorhandler(404)
    def page_not_found(e):
        return jsonify({
            "code": 404,
            "name": "Not Found",
            "description": "The requested URL was not found on the server.",
        }), 404
    return app
