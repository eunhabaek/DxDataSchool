#seq연산
msg="hello everyone"
print(msg[::]) #전체
print(msg[::]) #뒤에서 두번째 앞까지
print(msg[::-1]) #순서 반대

#문자열
#mgs[0]=k 문자열은 일부 변경 불가
number=10
string="ten=%d"%(number)
print(string)

print("ten={0}".format(number))
print(f"ten={number}")

#GCCG 찾기
problem="GDKSFSGCCGCCGGGGASADGCCGCCGASDAGA"
#위치 전부 출력
#한번 포함되면 그 문자열은 빼고 찾기
target="GCCG"
#print(target.find(problem))
pos=[]
i=0
while(i<len(problem)-3):
    if target.find(problem[i:i+4])!=-1:
        pos.append(i)
        i+=4
    i+=1
print(pos)

#시스템 인코딩 설정 확인
import sys
print(sys.stdin.encoding)
print(sys.stdout.encoding)

#문자열 인코딩/디코딩
print("한글".encode())
print("한글".encode().decode())

#문자열 바이트 변환
print(ord("a"),ord("A"),ord("가"))

#정규 표현식
import re
#:이나 |를 ,로 치환
targetstr="cat: dog: monkey| rabbit"
result=re.sub("[:,|]",",",targetstr)
print(result)

#유효한 이메일인지 검사
targetemail=["eunha@gmail.com","HI","안녕"]
p=re.compile("^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")

for email in targetemail:
    print(p.match(email)!=None)


#list의 메서드 활용
lst1=["cat","dog","rabbit","monkey","fox"]

#데이터 추가
lst1.append("lion")
lst1.insert(4,"mouse")
print(lst1)

#데이터 삭제
del lst1[1]
print(lst1)

#리스트 정렬 with key
lst1.sort(key=lambda x: x[1])
print(lst1)


#tuple
record=("eunha",27,"student")
print(record)

#unpacking
name, age, job1 =record
print(age)

*etc,job2=record
print(etc)

#swap- 두 개의 데이터 값 치환
a=10
b=20
a,b=b,a
print(a,b)

#tuple list
data=[("eunha",1),("crystal",2)]
for row in data:
    print(row[0])

#namedtuple
from collections import namedtuple
students=namedtuple("students","name age")
stu1=[students("eunha","27"),students("crystal","25")]
for i in stu1:
    print(i.name)

#set
animals={"cat","cat","dog"}
print(animals)

#set 순회
for i in animals:
    print(i)

#dict()
dic={}
dic["name"]="eunha"
dic["age"]=27
dic["job"]="student"
dic["job"]="singer" #job이 수정됨
print(dic)
#get
print(dic.get("address",0)) #존재하지 않는 key 사용 시 두번째 매개변수 리턴

#순회
for key in dic:
    print(key, dic[key])


#dto 역할을 수행하는 클래스 생성 -> 클래스 내 속성명 바꾸면 출력 시 문제 생김
#-> 요즘 선호함 code sense 동작 함

class Dto:
    def __init__(self,name="noname",tel="notel"):
        self.name=name
        self.tel=tel

dt1=[Dto("eunha","2409"),Dto("crystal","5705")]

#데이터 출력
for data in dt1:
    print(data.name,data.tel)

#dict를 이용한 mvc -> 속성명 바꿔도 출력에 문제 없음
#but code sense 적용 안됨
dt2=[{"name":"eunha","tel":"2409"},{"name":"crystal","tel":"5705"}]

for data in dt2:
    for key in data:
        print(key,":",data[key])

#이차원 배열 대신 dict 사용
group1=["orange","pink","blue"]
group2=["round","star","square"]

array1=[group1,group2] #list의 list
#list는 index를 이용 접근 => 내부 배열명 뽑기 불편함, 배열 추가 시 코드 고쳐야 함
#dict는 key 이용 접근

for idx,data in enumerate(array1):
    if idx==0:
        print("group1: ",end="\t")
    else:
        print("group2: ",end="\t")
    for elem in data:
        print(elem, end="\t")
    print()
#복잡하긴 하나, 이차원 배열 대신
array2=[{"name":"그룹1","data":group1},{"name":"그룹2","data":group2}]

for dic in array2:
    print(dic.get("name"),end=": ")
    for elem in dic.get("data"):
        print(elem, end="\t")
    print()



#list comprehension

li=list(range(10))

#li의 모든 데이터 제곱한 list 생성

#map 이용
re2=list(map(lambda x:x**2,li))
print(re2)

#list comprehension 이용
re3=[i**2 for i in li]
print(re3)

#list comprehension 응용 - 두개 리스트 이용
li1=[1,2,3]
li2=[4,5,6,7]

re=[x*y for x in li1 for y in li2]
print(re)

#for와 if 사용 => filtering
animals=["cat","dog","fig","lion","rabbit"]

#글자수 4이상 추출
#filter
re1=list(filter(lambda x:len(x)>=4,animals))
print(re1)

#list comprehension - with if
re2=list(x for x in animals if len(x)>=4)
print(re2)

#list comprehension - with if 2개 또는 and, or 사용 가능
re3=list(x for x in animals if len(x)>=4 if len(x)<5)
print(re3)

#list comprehension - with if else 문 활용
re4=list(x if len(x)<4 else x[0:3]+"..." for x in animals)
print(re4)

#Counter
from collections import Counter

data=["서울","경기","경기","서울","서울","부산","제주"]
counter=Counter(data)

print(dict(counter))
print(counter["서울"])

#상위 2개 추출
print(counter.most_common(2))

#합계 구하기
print(counter.total())

##튜플 합계구하기
fruits=[("apple",3),("apple",2),("orange",4),("orange",1),("mango",1)]
counter=Counter()

#합계 구하기
for name, count in fruits:
    counter[name]+=count
print(counter)

#예외처리 try except
def div(x):
    return 10/x

try:
    print(div(20))
    print(div(0))
except:
    print("예외 발생!")
print("프로그램 종료")
