#MariaDB연동
import pymysql

try:
    #데이터베이스 연결
    con = pymysql.connect(host='127.0.0.1', port=3306, user="root", password="000000", db="mysql", charset="utf8mb4")
    
    #sql실행 객체 생성
    cursor = con.cursor()

    #데이터 삽입 프로시저 실행
    cursor.callproc("myproc", args = ("jaes", "heo", 1998, "jeonju", "01088888888", "1998-04-06"))
    con.commit()
    print("프로시저실행 성공")
    cursor.execute("select * from usertbl")
except Exception as e:
    print(e)

finally:
    #연동 확인
    if 'con' in locals() and con.open:
        print(con, "MariaDB연동성공!")
        con.close()
        print("MariaDB연동을 종료합니다.")
