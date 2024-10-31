import pymysql
# con = pymysql.connect(host='127.0.0.1', port=3306, user="root", password="000000", db="mysql", charset="utf8mb4")
# print(con, "mariaDB 연결 성공!")
# con.close()
try:
    #데이터베이스 연결
    con = pymysql.connect(host='127.0.0.1', port=3306, user="root", password="000000", db="mysql")
    
    #sql실행 객체 생성
    cursor = con.cursor()

    #sql실행 - 삽입
    cursor.execute("insert into usertbl values('liy', 'sky', 1970, 'seoul', '01012345678', '1980-10-30')")
    cursor.execute("insert into usertbl values(%s, %s, %s, %s, %s, %s)", ('youngjin', 'kim', 2001, 'masan', '01026833842', '2001-07-09'))
    #DML수행내용 원본 데이터베이스에 반영
    con.commit()
    print("삽입성공")
    #sql실행 - 조회
    cursor.execute("select * from usertbl")
    #데이터 가져오기
    datas = cursor.fetchall()
    #가져온 데이터 읽기
    for data in datas:
         print(data)
except Exception as e:
    print(e)

finally:
    #연동 확인
    print(con, "MariaDB연동성공!")
    con.close()
    print("MariaDB연동을 종료합니다.")
