#获取聊天历史记录

import os
import mysql.connector
import json
from dotenv import load_dotenv

load_dotenv()

db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")

def returnManagerInformation():
    conn = mysql.connector.connect(
    host = db_host,       
    user = db_user,    
    password =db_password,  
    database="weather"  
)
    cursor = conn.cursor()
    cursor.execute("""
    SELECT 
        provinces.province_name, 
        cities.city_name, 
        districts.district_name, 
        districts.select_code
    FROM provinces
    JOIN cities ON cities.province_id = provinces.id
    JOIN districts ON districts.city_id = cities.id
""")
    results = cursor.fetchall()
    return_list = []
    for row in results:
        city_name = row[2]
        webpage_code = row[3]
        return_list.append((city_name,webpage_code))
    cursor.close()
    conn.close()
    return return_list
