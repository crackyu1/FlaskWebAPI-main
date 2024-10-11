from flask import Flask, render_template
app=Flask(__name__)
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/weather/China/<city>")
def get_weather_data(city):
    
    temperature=23

    return {
        "city":city,
        "temperature":temperature
    }
#如果访问的路径不存在，返回404
@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"),404


if __name__=="__main__":
    app.run(debug=True)