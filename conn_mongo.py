from pymongo import MongoClient

try:
    #데이터베이스 연결
    con = MongoClient("127.0.0.1", 27017)
    # 데이터베이스 연결 / 컬력션 생성 및 연결
    db = con.mymongo
    collect = db.user
    print("mongoDB와 연결이 되었습니다")
    
    #데이터 삽입1
    #collect.insert_one({"name": "example", "age": 30})

    #데이터 삽입2
    #doc1 = {'empno':'10001', 'name':'lim', 'phone':'011-0000-0000', 'addr':'busan'}
    #collect.insert_one(doc1)

    #데이터 삽입3
    doc2 = {'empno':'10002', 'name':'kim', 'phone':'012-0000-0000', 'addr':'masan'}
    doc3 = {'empno':'10003', 'name':'jim', 'phone':'013-0000-0000', 'addr':'jeju'}
    collect.insert_many([doc2, doc3])

    # 데이터 조회
    result = collect.find()
    for data in result:
        print(data)

except Exception as e:
    print("mongoDB연결 실패")
