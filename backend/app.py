from flask import Flask, jsonify, request
from flask_cors import CORS
from dotenv import load_dotenv
from returnWeatherInformation import *
from returnManagerInformation import *
from callGPTInterFace import *
import mysql.connector


app = Flask(__name__)
CORS(app)

load_dotenv()
db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_config = {
    'user':db_user, 
    'password':db_password, 
    'host': db_host,
    'database': 'default_database', 
}

def switch_database(new_database):
    db_config['database'] = new_database
    return mysql.connector.connect(**db_config)

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


@app.route('/api/getGPTResponse', methods=['POST'])
def getGPTResponse():
    user_id = request.form.get('user_id', '默认用户')
    model = request.form.get('model', 'gpt-3.5-turbo')
    user = request.form.get('user', '默认用户')
    text = request.form.get('text')
    max_tokens = request.form.get('max_tokens', 100)
    datetime = request.form.get('datetime')
    answertext = chat_with_gpt(user, text , max_tokens,model)
    if user_id != '默认用户':
        conn = switch_database('message')
        insertChatRecord(conn,user_id, datetime, text, answertext, model)
        conn.close()
    return answertext


@app.route('/api/getGPTHistory', methods=['POST'])
def getGPTHistory() ->list:
    user_id = request.form.get('user_id', '默认用户')
    user = request.form.get('user', '默认用户')
    conn = switch_database('message')
    respone_history = returnManagerInformation(conn,user)
    conn.close()
    return jsonify(respone_history)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

