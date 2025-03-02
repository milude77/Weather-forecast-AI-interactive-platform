#获取聊天历史记录
import os


current_dir = os.path.dirname(os.path.realpath(__file__))


# 获取历史聊天信息,通过用户ID
def returnManagerInformation(sql_connect,user_id) -> dict:
    conn = sql_connect
    cursor = conn.cursor(dictionary=True) 
    query = '''SELECT message,
                    timestamp,
                    is_sender
                FROM message 
                WHERE user_id = %s 
                ORDER BY timestamp ASC'''
    cursor.execute(query,(user_id,))
    chat_history = cursor.fetchall()
    return chat_history


#插入聊天记录
def insertChatRecord(sql_connect,user_id:int,datetime,message,sender:bool,model):
    try:
        conn = sql_connect  
        cursor = conn.cursor()
        sql = "INSERT INTO message (user_id,message,timestamp,is_sender,model_type) VALUES (%s,%s,%s,%s,%s)"
        val = (user_id,message,datetime,sender,model)
        cursor.execute(sql,val)
        conn.commit()
    except Exception as e:
        print(e)

def delhistoryMessage(sql_connect,user_id:int):
    try:
        conn = sql_connect  
        cursor = conn.cursor()
        sql = "DELETE FROM message WHERE user_id = %s"
        cursor.execute(sql,(user_id,))
        conn.commit()
    except Exception as e:
        print(e)
        


