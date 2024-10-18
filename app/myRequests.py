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
    response=requests.get(url)
    #获取response的text
    if hasattr(response.request, 'text'):
        mytext=response.request.text
        #mytext中包含"code":400,直接抛出mytext\
        if '"code":400' in mytext:
            raise Exception(mytext)
       
        
    #获取json数据
    data=response.json()
    try: 
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