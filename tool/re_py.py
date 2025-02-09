#使用此脚本批量获取地区及其网页地址，并插入到数据库中。

import re
import mysql.connector

hear ='<dd id="cityList_city"><a href="http://www.weather.com.cn/weather1d/101071401.shtml#search" title="葫芦岛">葫芦岛</a><a href="http://www.weather.com.cn/weather1d/101071402.shtml#search" title="建昌">建昌</a><a href="http://www.weather.com.cn/weather1d/101071403.shtml#search" title="绥中">绥中</a><a href="http://www.weather.com.cn/weather1d/101071404.shtml#search" title="兴城">兴城</a><a href="http://www.weather.com.cn/weather1d/101071405.shtml#search" title="连山">连山</a><a href="http://www.weather.com.cn/weather1d/101071406.shtml#search" title="龙港">龙港</a><a href="http://www.weather.com.cn/weather1d/101071407.shtml#search" title="南票">南票</a></dd>'
pattern = re.compile(r'weather1d/(\d+)\.shtml[^>]+title="([^"]+)"')
matches = pattern.findall(hear)
result = [{"code": code, "name": name} for code, name in matches]
values = [(item["name"],item["code"]) for item in result]



'''hear = '<dd id="cityList_city"><a href="javascript:void(0);" data-city="辽宁" title="沈阳">沈阳</a><a href="javascript:void(0);" data-city="辽宁" title="大连">大连</a><a href="javascript:void(0);" data-city="辽宁" title="鞍山">鞍山</a><a href="javascript:void(0);" data-city="辽宁" title="抚顺">抚顺</a><a href="javascript:void(0);" data-city="辽宁" title="本溪">本溪</a><a href="javascript:void(0);" data-city="辽宁" title="丹东">丹东</a><a href="javascript:void(0);" data-city="辽宁" title="锦州">锦州</a><a href="javascript:void(0);" data-city="辽宁" title="营口">营口</a><a href="javascript:void(0);" data-city="辽宁" title="阜新">阜新</a><a href="javascript:void(0);" data-city="辽宁" title="辽阳">辽阳</a><a href="javascript:void(0);" data-city="辽宁" title="铁岭">铁岭</a><a href="javascript:void(0);" data-city="辽宁" title="朝阳">朝阳</a><a href="javascript:void(0);" data-city="辽宁" title="盘锦">盘锦</a><a href="javascript:void(0);" data-city="辽宁" title="葫芦岛">葫芦岛</a></dd>'
pattern = re.compile(r'title="([^"]+)"')
matches = pattern.findall(hear)
result = [name for name in matches]'''

# 连接到 MySQL 数据库
conn = mysql.connector.connect(
    host="localhost",          # MySQL 主机
    user="root",      # 数据库用户名
    password="huayuan5166",  # 数据库密码
    database="weather"   # 数据库名称
)

# 创建游标
cursor = conn.cursor()

# 插入数据的 SQL 语句
sql = "INSERT INTO districts (district_name,city_id,select_code) VALUES (%s,14,%s)"

for i in range(1,len(result)+1):
    # 批量插入数据
    try:
        cursor.execute(sql, (values[i-1][0],values[i-1][1]))
        conn.commit()  # 提交事务
        print(f"{cursor.rowcount} 条记录已插入。")
    except mysql.connector.Error as err:
        print(f"发生错误: {err}")
        conn.rollback()  # 如果出错，回滚事务

