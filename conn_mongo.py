from pymongo import MongoClient

try:
    #데이터베이스 연결
    con = MongoClient("127.0.0.1", 27017)
    # 데이터베이스 연결 / 컬력션 생성 및 연결
    db = con.mymongo
    collect = db.user
    print("mongoDB와 연결이 되었습니다")
    # 데이터 삽입
    collect.insert_one({"name": "example", "age": 30})
    # 데이터 조회
    result = collect.find()
    for data in result:
        print(data)

except Exception as e:
    print("mongoDB연결 실패")
