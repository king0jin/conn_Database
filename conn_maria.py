import pymysql

con = pymysql.connect(host='127.0.0.1', port=3306, user="root", password="000000", db="mysql", charset="utf8mb4")

print(con, "mariaDB 연결 성공!")
con.close()