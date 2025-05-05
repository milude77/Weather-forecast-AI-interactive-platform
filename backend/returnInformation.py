import os
import json

current_directory = os.path.dirname(os.path.abspath(__file__))  
fixed_directory = os.path.join(current_directory, "..")
weather_file_path = os.path.join(fixed_directory,"datafile","weather.json")
city_file_path = os.path.join(fixed_directory,"datafile","city.json")

#查询天气json文件中的数据
def returnWeatherInformation(data:str) -> list:
    with open(weather_file_path, 'r',encoding='utf-8') as f:
        weather_data = json.load(f)
        return weather_data[data]

#查询城市json文件中的数据
def returnCityInformation() -> dict:
    with open(city_file_path, 'r',encoding='utf-8') as f:
        city_data = json.load(f)
    return city_data

def returnAllCityWeather() -> list:
    with open(weather_file_path, 'r',encoding='utf-8') as f:
        weather_data = json.load(f)
    return weather_data




