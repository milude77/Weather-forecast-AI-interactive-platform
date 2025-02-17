import os
import jwt
import bcrypt
import datetime
import mysql.connector
from flask import Flask, jsonify, request
from flask_cors import CORS
from dotenv import load_dotenv
from returnWeatherInformation import *
from returnManagerInformation import *
from callGPTInterFace import *

app = Flask(__name__)

CORS(app)

load_dotenv()
db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
secret_key = os.getenv("SECRET_KEY")

db_config = {
    'user':db_user, 
    'password':db_password, 
    'host': db_host,
    'database': 'default_database', 
}

#更改数据库连接
def switch_database(new_database):
    db_config['database'] = new_database
    return mysql.connector.connect(**db_config)

#哈希加密
def hash_password(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password

#验证密码
def verify_password(password, hashed_password):
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))


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
    data = request.get_json()  # 获取 JSON 数据
    user_id = data.get('user_id', '默认用户')
    model = data.get('model', 'gpt-3.5-turbo')
    user = data.get('user', 'user')
    text = data.get('text')
    max_tokens = data.get('max_tokens', 200)
    datetime = request.form.get('datetime')
    answertext = chat_with_gpt(user, text,max_tokens,model)
    if user_id != '默认用户':
        conn = switch_database('message')
        insertChatRecord(conn,user_id, datetime, text, answertext, model)
        conn.close()
    print(answertext)
    return answertext


@app.route('/api/getGPTHistory', methods=['POST'])
def getGPTHistory() ->list:
    user_id = request.form.get('user_id', '默认用户')
    user = request.form.get('user', '默认用户')
    conn = switch_database('message')
    respone_history = returnManagerInformation(conn,user_id)
    conn.close()
    return jsonify(respone_history)


@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json() 
    email = data.get('email')
    password = data.get('password')
    conn = switch_database('user')
    cursor = conn.cursor(dictionary=True)
    query = "SELECT * FROM users WHERE email = %s"
    cursor.execute(query,(email,))
    user_info = cursor.fetchone()
    conn.close()
    if user_info:
        if verify_password(password, user_info['password']):
            payload = {
                'user_id': user_info['id'],
                'exp': datetime.datetime.now() + datetime.timedelta(hours=1)
            }
            token = jwt.encode(payload, secret_key, algorithm='HS256')

            return jsonify({'success': True, 'token': token ,'message': '登录成功'}) , 200
        else:
            return jsonify({'message': '用户名或密码错误'}), 401
    else:
        return jsonify({'message': '用户名或密码错误'}), 401

@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()  
    username = data.get('username')
    email = data.get('email')       
    password = hash_password(data.get('password'))
    conn = switch_database('user')
    cursor = conn.cursor(dictionary=True)
    try:
        query = "INSERT INTO users (email, password ,name) VALUES (%s, %s, %s)"
        cursor.execute(query,(email,password,username))
        conn.commit()
    except mysql.connector.Error as err:
        if err.errno == 1062:
            return jsonify({'message': '邮箱已注册'}), 400
        else:
            print(err)
            return jsonify({'message': '注册失败'}), 500
    conn.close()
    return jsonify({'message': '注册成功'}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

