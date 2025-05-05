import os
import traceback
import requests
import mysql.connector
import json
import datetime
from bs4 import BeautifulSoup
from dotenv import load_dotenv

fixed_directory = "/Weather-forecast-and-GPT-chat-platform"
file_path = os.path.join(fixed_directory, "weather.json")
env_path = os.path.join(fixed_directory,'config','mysql_config.env')
fixed_directory = "/Weather-forecast-and-GPT-chat-platform"

env_path = os.path.join(fixed_directory,'config','mysql_config.env')
load_dotenv(dotenv_path=env_path)

db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")

print(db_host, db_user, db_password)