from flask import Flask, jsonify, request
from flask_cors import CORS
from returnWeatherInformation import *
from returnWeatherInformation import *
from callGPTInterFace import *


app = Flask(__name__)
CORS(app)

# 模拟天气数据的接口
@app.route('/api/getDistrictweather', methods=['GET'])
def get_district_weather():
    city = request.args.get('city', '沈阳')  # 获取用户选择的城市
    weather_data = returnWeatherInformation(city)  # 获取天气数据
    return jsonify(weather_data)


# 获取城市数据的接口
@app.route('/api/city', methods=['GET'])
def get_city():
    city_data = returnCityInformation()  
    return jsonify(city_data)


# 获取所有城市数据的接口
@app.route('/api/getAllcityweather', methods=['GET'])
def getAllcityweather():
    city_data = returnAllCityWeather()  
    return jsonify(city_data)


@app.route('/api/getGPT3.5', methods=['POST'])
def getGPT3_5():
    user = request.form.get('user', '默认用户')
    text = request.form.get('text', '你好，请问有什么可以帮助您？')
    max_tokens = request.form.get('max_tokens', 100)
    answertext = chat_with_gpt3(user, text , max_tokens)
    return answertext


@app.route('/api/getGPT4o', methods=['POST'])
def getGPT4o():
    user = request.form.get('user', '默认用户')
    text = request.form.get('text', '你好，请问有什么可以帮助您？')
    max_tokens = request.form.get('max_tokens', 100)
    answertext = chat_with_gpt4o(user, text , max_tokens)
    return answertext

@app.route('/api/getGPTHistory', methods=['POST'])
def getGPTHistory() ->list:
    user = request.form.get('user', '默认用户')
    respone_history = returnManagerInformation(user)
    return jsonify(respone_history)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

