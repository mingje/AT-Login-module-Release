import mysql.connector

"""
#建立資料庫
condb = mysql.connector.connect(host="10.64.101.42",user="root", passwd="admin")
cur = condb.cursor()
SQL="CREATE DATABASE IF NOT EXISTS MobileTest DEFAULT CHARSET=utf8 DEFAULT COLLATE=utf8_unicode_ci"
cur.execute(SQL)
"""
#建立表單
condb = mysql.connector.connect(host="10.64.101.42",user="root", passwd="admin", db="MobileTest", charset="utf8")
cursor = condb.cursor()
#SQL="CREATE TABLE IF NOT EXISTS APPtest(MissionID INT(11) PRIMARY KEY AUTO_INCREMENT, Classification text,\
#CaseID text, StartTime DATETIME, EndTime DATETIME, Result VARCHAR(20))"
#新增資料
SQL="INSERT INTO APPtest(MissionID,Classification,CaseID,StartTime,EndTime,Result) VALUES('2','Login','ForTest1',\
   '2019-01-17 13:17:20','2019-01-17 13:30:20','FAIL')"
cursor.execute(SQL)
condb.commit()
cursor.close()
condb.close()
