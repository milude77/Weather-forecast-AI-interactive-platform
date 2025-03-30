import os
import requests
import mysql.connector
import json
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from time import sleep


for i in range(1, 1000):
    sleep(0.1)
    print(f"\r{i}/1000",end="")