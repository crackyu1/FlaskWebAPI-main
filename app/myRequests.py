#访问url https://goweather.herokuapp.com/weather/Haerbin并解析返回的json数据
import requests
#url可变，通过传入url参数获取json数据

def get(province:str,city:str):
    url = f"https://cn.apihz.cn/api/tianqi/tqyb.php?id=88888888&key=88888888&sheng={province}&place={city}"
    response=requests.get(url)
    #获取json数据
    data=response.json()
    #获取json数据中的place和temperature
    #添加try except语句，如果json数据中没有place和temperature则返回到main.errorhandler(400)中 
    try:
        place=data["place"]
        temperature=data["temperature"]
        weather=data["weather1"]

    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"输入的城市有误: {e}")
    #作为list返回
    return [place,temperature,weather]

    #return {"place":place,"temperature":temperature,"weather":weather}

if __name__=="__main__":
    dict=get(province="广东",city="广州")
    print(dict)