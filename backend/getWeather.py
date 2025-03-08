#获取目标地区的天气信息
import os
import requests
import mysql.connector
import json
import datetime
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")

fixed_directory = "/Weather-forecast-and-GPT-chat-platform"

os.makedirs(fixed_directory, exist_ok=True)

file_path = os.path.join(fixed_directory, "weather.json")

#获取地区对应的网页码
def storeWeatherData() -> list:
    conn = mysql.connector.connect(
    host= db_host,          # MySQL 主机
    user= db_user,      # 数据库用户名
    password= db_password,  # 数据库密码
    database="weather"   # 数据库名称
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

#获取天气数据
def getWeatherData(webpage_code: str) -> dict:
    url = f"http://www.weather.com.cn/weather/{webpage_code}.shtml"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    weather_list = []
    for li in soup.select(".t.clearfix li"):
        day = li.find("h1").get_text(strip=True)
        wea = li.find("p", class_="wea").get_text(strip=True)
        tem = li.find("p", class_="tem").get_text(strip=True).replace("\n", "").replace("\r", "")
        wind = li.find("p", class_="win").get_text(strip=True).replace("\n", "").replace("\r", "")
        weather_list.append({"day": day, "wea": wea, "tem": tem, "wind": wind})

    return weather_list

if __name__ == "__main__":
    city_list = storeWeatherData()
    print("获取地区代码完成")
    weather_content = {}
    for city_name, webpage_code in city_list:
        try:
            weather_data = getWeatherData(webpage_code)
            weather_content[city_name] = weather_data
            #print(f"{city_name} 成功获取")
        except error as e:  
            print(f"{city_name} 获取失败")
    with open(file_path, "w", encoding="utf-8") as f:
        now_time = datetime.datetime.now()
        print(f"更新时间 {now_time}")
        json.dump(weather_content, f, ensure_ascii=False)
        
        
