import os
import json

#查询天气json文件中的数据
def returnWeatherInformation(data:str) -> list:
    current_dir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join('..', 'weather.json')
    with open(os.path.join(current_dir, file_path), 'r',encoding='utf-8') as f:
        weather_data = json.load(f)
        return weather_data[data]

#查询城市json文件中的数据
def returnCityInformation() -> dict:
    current_dir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join('..', 'city.json')
    with open(os.path.join(current_dir, file_path), 'r',encoding='utf-8') as f:
        city_data = json.load(f)
    return city_data

#返回所有城市城区的天气信息
def returnAllCityWeather() -> list:
    current_dir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join('..', 'weather.json')
    with open(os.path.join(current_dir, file_path), 'r',encoding='utf-8') as f:
        weather_data = json.load(f)
    return weather_data



