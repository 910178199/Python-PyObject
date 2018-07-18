#!/usr/bin/python3

import pymysql

# 打开数据库连接
db = pymysql.connect("localhost", "root", "123456", "FREEBUF_DATA")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询
# cursor.execute("SELECT VERSION()")

# 创建表
# 如果存在employee表则删除
# cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
# 创建表语句
# createSql = """CREATE TABLE EMPLOYEE(
#     FIRST_NAME CHAR(20) NOT NULL,
#     LAST_NAME CHAR(20),
#     AGE INT,
#     SEX CHAR(1),
#     INCOME FLOAT,
#     MONEY FLOAT)"""
# cursor.execute(createSql)

# 增加数据
# insertSql = """INSERT INTO EMPLOYEE(
#     FIRST_NAME,LAST_NAME,AGE,SEX,INCOME,MONEY)
#     VALUES('WINDOWS','HOMIN',22,'M',3000,9999)"""

insertSql = "INSERT INTO NEWS(TITLE,URL,IMGURL,CONTENT) VALUES ('%s','%s','%s','%s')" % (
    "title", "sdfsdf", "sdfsdf", "sdfd")


# 查询数据
# cursor.execute("use testdb")
# cursor.execute("select * from EMPLOYEE")

# 条件查询
# conditionQueraSql = "SELECT * FROM EMPLOYEE WHERE MONEY > '%d'" % (1000)
# try:
#     #执行sql语句
#     cursor.execute(conditionQueraSql)
#     #获取所有记录列表
#     results = cursor.fetchall()
#     for row in results:
#         fname = row[0]
#         lname = row[1]
#         age = row[2]
#         sex = row[3]
#         income = row[4]
#         money = row[5]
#         #打印结果
#         print("fname = %s,lname = %s ,age = %d , sex = %s,income = %d,money = %d" %
#          (fname,lname,age,sex,income,money))

# except:
#     print ("Error: unable to fetch data")


# 使用 fetchone() 方法获取单条数据.
# data = cursor.fetchall()

# print("Database version : %s " % data)
# print("查询数据：")
# print(data)
# print(end='\n')

try:
    # 执行插入sql语句
    cursor.execute(insertSql)
    # 提交
    db.commit()
except:
    # 如果发生错误
    db.rollback()

# 关闭数据库连接
db.close()
