import os
from dotenv import load_dotenv
import mysql.connector
import datetime
import jwt
import bcrypt
import json


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

def hash_password(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password

#更改数据库连接
def switch_database(new_database):
    db_config['database'] = new_database
    return mysql.connector.connect(**db_config)

def verify_password(password, hashed_password):
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))

email =('11111111@qq.com',)
password = '11111111'
conn = switch_database('user')
cursor = conn.cursor(dictionary=True)
query = "SELECT * FROM users WHERE email = %s"
cursor.execute(query,email)
user_info = cursor.fetchone()
if user_info:
    if verify_password(password, user_info['password']):
        payload = {
            'user_id': user_info['id'],
            'exp': datetime.datetime.now() + datetime.timedelta(hours=1)
        }
        token = jwt.encode(payload, secret_key, algorithm='HS256')
        print('登陆成功')
        print(token)
    else:
        print('密码错误')