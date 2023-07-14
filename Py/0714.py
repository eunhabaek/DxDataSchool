##예외 처리 2
arr=list(range(0,40,10))
try:
    number=int(input("나눌 정수를 입력하세요: "))
    lens=len(arr)
    i=0
    while i<lens:
        if number==1:
            raise ValueError("강제 예외발생") # 1 입력 시 강제로 예외 발생
        assert number!=2, "2는 안됩니다." #2 입력 시 assertion 진행
        print(arr[i]/number)
        i+=1
except ValueError as ve: #정수 입력하지 않을 시 예외처리
    print(ve)
    print("잘못된 데이터입니다. 정수를 입력하세요.")
except ZeroDivisionError as zde: #0 입력 시 예외처리
    print(zde)
    print("0이 아닌 정수를 입력하세요.")
else:
    print("예외 발생하지 않음")
finally:
    print("프로그램 종료")

#file handling

import os

print(os.getcwd()) #현재 작업디렉토리 경로 확인

try:
    #파일 쓰기
    file=open('./data/test.txt','w',encoding="utf8")
    file.write("hello") #file에 내용 쓰기

    lines=["cats\n","dogs\n","monkeys\n","안녕"]
    file.writelines(lines)

    #파일 읽기
    with open('./data/test.txt','r',encoding="utf8") as file:

        #줄단위로 읽기
        for line in file:
            print(line)
            print()

    #content=file.read() #file 내용 전체 읽기
    #print(content)

except Exception as e: #예외 처리
    print("파일 읽기 중 에러: ",e)


#csv 읽기
#1. 텍스트로 읽어서 split 이용
data=[]
with open('./data/경기도_이천시_지역화폐발행 및 이용현황_20221015.csv','r') as csv1:
    for line in csv1:
        ar=line.split(",")
        data.append(ar)
print(data)

#2. 파이썬 csv 모듈 이용
import csv

#csv 읽기
data=[]
with open('./data/경기도_이천시_지역화폐발행 및 이용현황_20221015.csv','r') as csv1:
    csv2=csv.reader(csv1)
    for line in csv2:
        data.append(ar)
print(data)

#csv 쓰기
import csv
with open('./data/test_0714.csv','w') as wt:
    wr=csv.writer(wt)
    wr.writerow(["cat","dog","monkey"])
    wr.writerow(["mouse","rabbit","lion"])

#바이너리 파일 써보기. 문자열 보다는 이미지 저장용
with open("./data/test_0714.bin",'wb') as file:
    file.write('안녕하세요'.encode())
with open("./data/test_0714.bin",'rb') as file:
    content=file.read()
    print(content.decode())

#dto class 생성
class DTO:
    def __init__(self,number=0,name="noname"):
        self.__number=number
        self.__name=name
    @property
    def number(self):
        return self.__number
    @property
    def name(self):
        return self.__name
    @number.setter
    def number(self,number):
        self.number=number
    @name.setter
    def name(self,name):
        self.name=name

    #인스턴스를 print 함수에 대입 시 호출되는 메서드 - 오버라이딩
    #디버깅 목적으로 값 확인 위해 쓰임
    def __str__(self):
        return str(self.__number)+":"+self.__name

#파일에 기록할 데이터 생성
dto1=DTO(1,"eunha")
dto2=DTO(2,"crystal")

print(dto1)
print(dto2)

import pickle
#인스턴스 파일 생성
try:
    #serializing
    with open("./data/data.date","wb") as file:
        pickle.dump(dto1,file)

    # 만들어진 파일 deserializing 하지 않으면 읽지 못함
    with open("./data/data.date", "rb") as file:
        result=pickle.load(file)
        print(result)
        #for dt in result:
        #    print(dt)

except Exception as e:
    print(e)

##zipfile 압축/해제
import zipfile

#압축할 데이터 리스트 만들기
filelst=['./data/test_0714.bin','./data/test_0714.csv']

#zip 압축하기
with zipfile.ZipFile('./data/test_0714.zip','w') as myzipf:
    for f in filelst:
        myzipf.write(f)
#zip 압축 해제
zipfile.ZipFile('/data/test_0714.zip').extractall()

#접속 성공 횟수 출력
logs=[]
cnt=0
with open('./data/log.txt','r') as log:
    for i in log:
        sub=i.split(' ')
        if sub[8]=="200":
            cnt+=1
        #logs.append(i.split(' '))
print(cnt)

#ip별 접속 횟수
logs={}
with open('./data/log.txt','r') as log:
    for i in log:
        sub=i.split(' ')
        logs[sub[0]]=logs.get(sub[0],0)+1
print(logs)


#ip별 트래픽 수
logs={}
with open('./data/log.txt','r') as log:
    for i in log:
        sub=i.strip("\n").split(' ')
        try:
            logs[sub[0]]=logs.get(sub[0],0)+int(sub[9])
        except Exception as e:
            print(e)
print(logs)

#Counter 이용하기
from collections import Counter
logs=Counter()
with open('./data/log.txt','r') as log:
    for i in log:
        sub=i.strip("\n").split(' ')
        try:
            logs[sub[0]]=logs.get(sub[0],0)+int(sub[9])
        except Exception as e:
            print(e)
print(logs)
print(logs.most_common(10))