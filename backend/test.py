import os
import traceback
import requests
import mysql.connector
import json
import datetime
from bs4 import BeautifulSoup
from dotenv import load_dotenv




db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")

print(db_host, db_user, db_password)