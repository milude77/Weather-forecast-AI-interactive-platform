#获取聊天历史记录

import os
import mysql.connector
import json
from dotenv import load_dotenv



# 获取历史聊天信息
def returnManagerInformation(sql_connect,user) -> list:
    conn = sql_connect
    cursor = conn.cursor(dict_cursor=True)
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
    return 


#插入聊天记录
def insertChatRecord(sql_connect,user,datetime,message):
    conn = sql_connect  
