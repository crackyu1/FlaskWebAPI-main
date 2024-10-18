#访问url https://goweather.herokuapp.com/weather/Haerbin并解析返回的json数据
from flask import abort
import requests
#url可变，通过传入url参数获取json数据
class WeatherRequestError(Exception):
    def __init__(self, message, province, city):
        super().__init__(message)
        self.province = province
        self.city = city
def get(province:str,city:str):
    url = f"https://cn.apihz.cn/api/tianqi/tqyb.php?id=88888888&key=88888888&sheng={province}&place={city}"
    try:
        response=requests.get(url)
        response.raise_for_status()
        #获取json数据
        data=response.json() 
        place=data["place"]
        temperature=data["temperature"]
        weather=data["weather1"]
    except KeyError as e:
        raise WeatherRequestError(f"查不到:{province}{city}的天气数据", province, city)
    #作为list返回
    return [place,temperature,weather]

    #return {"place":place,"temperature":temperature,"weather":weather}

if __name__=="__main__":
    dict=get(province="广东",city="广州")
    print(dict)