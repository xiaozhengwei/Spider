#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pymysql
import pandas as pd

# 打开数据库连接
db = pymysql.connect("47.93.221.205", "root", "1998zh2003", "utunan", charset='utf8' )

# 使用cursor()方法获取操作游标
cursor = db.cursor()
state=0

values=pd.read_csv("school_info.csv").values
def insert_major_info(value):
    # SQL 插入语句
    sql = """INSERT INTO direction(schoolName,collegeName,majorlName,directionName, degreeType,politics,english,math,majorBasics)
             VALUES ('{}', '{}','{}','{}','{}','{}','{}','{}','{}')""".format(value[0],value[2],value[3],value[4],"学硕(理科)",value[5],value[6],value[7],value[8]);

    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        print(value)
        pass

for value in values:
    insert_major_info(value)