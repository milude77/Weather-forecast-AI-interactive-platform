#获取聊天历史记录
import os
import json
import logging


current_dir = os.path.dirname(os.path.realpath(__file__))




# 获取历史聊天信息,通过用户ID
def returnManagerInformation(sql_connect,user_id) -> list:
    conn = sql_connect
    cursor = conn.cursor(dict_cursor=True)
    cursor = sql_connect.cursor(dictionary=True)  # 以字典格式返回数据
    query = "SELECT * FROM message WHERE user_id = %s ORDER BY timestamp ASC"
    cursor.execute(query,(user_id))
    chat_history = cursor.fetchall()
    return chat_history


#插入聊天记录
def insertChatRecord(sql_connect,user_id,datetime,message,answer,model):
    try:
        conn = sql_connect  
        cursor = conn.cursor()
        sql = "INSERT INTO message (user_id,datetime,message,answer,model) VALUES (%s,%s,%s,%s,%s)"
        val = (user_id,datetime,message,answer,model)
        cursor.execute(sql,val)
    except:
        print("Error inserting chat record")


