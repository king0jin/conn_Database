#MariaDB연동
import pymysql

try:
    #데이터베이스 연결
    con = pymysql.connect(host='127.0.0.1', port=3306, user="root", password="000000", db="mysql", charset="utf8mb4")
    
    #sql실행 객체 생성
    cursor = con.cursor()

    #삽입할 사진 파일 내용 읽어오기
    filename = r"C:\Users\et070\OneDrive\Desktop\image\macaron.jpg"
    f = open(filename, 'rb')
    photo = f.read()
    f.close()
    cursor.execute('insert into blobtable values(%s, %s, %s)', args = ('cheese', filename, photo))
    con.commit()

    filename = r"C:\Users\et070\OneDrive\Desktop\image\brown.webp"
    f = open(filename, 'rb')
    photo = f.read()
    f.close()
    cursor.execute('insert into blobtable values(%s, %s, %s)', args = ('macaron', filename, photo))
    con.commit()

    #사진 파일 읽어오기
    cursor.execute('select * from blobtable')
    datas = cursor.fetchall()
    for data in datas:
        f = open(data[1], "wb")
        f.write(data[2])
        f.close()
    con.commit()
except Exception as e:
    print(e)

finally:
    con.close()        
    #연동확인
    # print(con)
