import os
import requests
import mysql.connector
import json
from bs4 import BeautifulSoup
from dotenv import load_dotenv


fixed_directory = "/Weather-forecast-and-GPT-chat-platform"

# 确保目录存在
os.makedirs(fixed_directory, exist_ok=True)

# 定义文件路径
file_path = os.path.join(fixed_directory, "weather.json")

if __name__ == "__main__":
    with open(file_path, "w", encoding="utf-8") as f:
        f.write("hello")