##pyMySQL 설치하기
##cmd에서 pip install pyMySQL
import pymysql
import sys
try:
    #연결 객체 생성
    connect=pymysql.connect(host='localhost',port=3306,db='mysql',
                            user='root',passwd='beh1016',charset='utf8')
    #SQL 실행 객체 생성
    cursor=connect.cursor()

    cursor.execute("USE dx0717")
    # SQL insert 실행 (1) - 값 직접 sql에 작성
    cursor.execute("INSERT INTO DEPT VALUES(14,'인사관리','서울');")

    # SQL update 실행 (2) - 서식 설정하여 대입
    cursor.execute("UPDATE DEPT SET DNAME=%s, LOC=%s WHERE DEPTNO=%s;",('개발','부산',11))

    # SQL delete 실행 (3) - 서식 설정하여 대입
    cursor.execute("DELETE FROM DEPT WHERE DEPTNO=%s;",14)

    # SQL DQL (4) - 서식 설정하여 대입
    cursor.execute("SELECT * FROM DEPT WHERE DEPTNO >5;")

    record=cursor.fetchall()
    if len(record)==0:
        print('검색된 데이터 없음')
    else:
        for elem in record:
            print(elem)
    #원본에 반영
    connect.commit()

    print(connect)
except:
    print("pyMySQL 예외 발생!!",sys.exc_info())
finally:
    if connect !=None:
        connect.close()




import pymysql
import sys
try:
    #연결 객체 생성
    connect=pymysql.connect(host='localhost',port=3306,db='mysql',
                            user='root',passwd='beh1016',charset='utf8')
    #SQL 실행 객체 생성
    cursor=connect.cursor()

    cursor.execute("USE dx0717;")

    # 삽입할 이미지
    f=open('./MySQL/zzanggu.jpg','rb')
    zzang=f.read()
    f.close()

    #데이터 삽입
    cursor.execute("INSERT INTO FILETB VALUES(%s,%s);",('zzanggu.jpg',zzang))
    connect.commit()

    #데이터 읽어오기
    cursor.execute("SELECT * FROM FILETB")
    data=cursor.fetchone()

    #두번째 데이터가 blob이므로 두번째 데이터를 파일로 변경
    print(data[0]) #파일명

    #파일 쓰기 모드로 생성
    f = open(data[0],'wb')

    #읽은 데이터 파일에 기록
    #f.write(data[1])
    f.read(data[1])
    f.close()

    connect.commit()
except:
    print("pyMySQL 예외 발생!!",sys.exc_info())
finally:
    if connect !=None:
        connect.close()


