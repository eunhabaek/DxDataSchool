#람다 예시1
lst=[i for i in range(100000)] #0-99999까지

#1. 숫자 리스트로 제곱
temp=[]
for x in lst:
    temp.append(x*x)
print(temp)

#2. 1번 연산을 함수로
def f(x):
    return x*x

temp=list(map(f,lst))
print(temp)

#3. 2번에 함수를 람다로
temp=list(map(lambda x:x*x,lst))
print(temp)



# 3글자 이상이면 ...처리하기
animals=["cat","dog","rabbit","monkey"]

def ext(x):
    if len(x)>3:
        return x[0:3]+"..."
    return x

results=list(map(ext,animals))
print(results)


##filter 예시 1

colors=["red","orange","pink","blue",None]

#결측치 확인
print(None in colors)

#결측치 제거
def no_na(x):
    return x !=None

#이름 3> 만 추출

def len3(x):
    return len(x)>=3


colors0=list(filter(no_na,colors))
result=list(filter(len3,colors0))

#lambda 이용 실습
colors0=list(filter(lambda x:x!=None,colors))
result2=list(filter(lambda x:len(x)>=3,colors0))


print(result)
print(result2)


#한글 자음으로 filtering
#ㄱ으로 시작하는 요소 추출하기 ("가"<=X<"나")
name=["고래","강아지","고양이","사자","호랑이"]

def checkk(x):
    if x[0]<"나" and x[0]>="가":
        return x

temp=list(filter(checkk,name))

#lambda 이용
temp2=list(filter(lambda x:x[0]<"나" and x[0]>="가",name))

print(temp)
print(temp2)


#in ,not in 예시
#일치
numbers=["1","2","3","4"]
except_num=["2"]

temp=list(filter(lambda x:x not in except_num,numbers))
print(temp)

#포함되는지
print("ab".find("a"))

#reduce
from functools import reduce

result=reduce(lambda x,y:x*y,[1,2,3,4])
print(result)


##zip 예시

school=["초등학교","중학교","고등학교"]
school_name=["광주","탄벌","양서"]

print(list(zip(school,school_name)))
print(dict(zip(school,school_name)))

#중첩함수, local, nonlocal, global

def outer():
    str_out="outer printing"
    def inner():
        str_in="inner printing"
        nonlocal str_out #이 문장 작성하지 않으면 로컬로 인식하여 에러남
        print(str_out)

        str_out="change" #외부 함수 데이터는 읽기만 가능
        print(str_out)

    #print(str_in) #내부 함수 데이터는 외부 함수에서 접근 불가
    inner()
    print(str_out)

outer()
#inner() #내부 함수는 외부 함수 밖에서 접근 불가

## closure 예제

def outer():
    outer_data=0

    #외부 함수의 데이터를 수정하는 내부 함수
    def inner():
        nonlocal outer_data
        outer_data+=1
        print(outer_data)
    return inner

closure=outer()

closure()
closure()

#모듈화 =>이후 파일로 분리
def commonconcern1():
    print("common concern 1")

def commonconcern2():
    print("common concern 2")

def businesslogic():
    print("business logic 1")
def transaction():
    commonconcern1()
    businesslogic()
    commonconcern2()

##데코레이터 1 이용
def deco(func):
    def wrapper():
        print(func.__name__, '함수 시작')  # __name__으로 함수 이름 출력
        func()  # 매개변수로 받은 함수를 호출
        print(func.__name__, '함수 끝')
    return wrapper
@deco
def businesslogic2():
    print("business logic 1")

businesslogic2()


##데코레이터 2
import time
def clock(func):
    #decorator 호출 시 수행될 함수
    def innerclock(*args):
        start = time.time()
        result=func(*args)
        end = time.time()
        elapsed = end - start
        print("수행시간: ",elapsed) #수행시간
        print("매개변수: ",args) #매개변수
        print("리턴값: ",result) #리턴값
        return result

    return innerclock

@clock
def koreanAge(age):
    return age+2

print(koreanAge(25))

##메서드 호출 예제

class Student:
    class_data="클래스 속성" #클래스 속성 만들기

    #메서드 만들기
    def disp(self):
        print("인스턴스 생성")

    #속성 생성
    def setName(self,name):
        self.name=name #self.name은 인스턴스의 속성

#인스턴스 생성
stu=Student() #재사용 용이

#메서드 호출
#1. bound 호출
stu.disp()
Student().disp()

#2.unbound 호출
Student.disp(stu)

#인스턴스 속성 생성
stu.setName("eunha")

print(Student.class_data) #클래스명으로 클래스 속성 접근
print(stu.class_data) #인스턴스명으로 클래스 속성 접근

#클래스명 클래스 속성 수정
Student.class_data="클래스 데이터 수정"
Student.class_new_data="클래스 데이터 생성"
print(Student.class_data)
print(stu.class_data)

#인스턴스명 클래스 속성 재수정
stu.class_data="클래스 데이터 재수정"
print(Student.class_data)
print(stu.class_data) #인스턴스 안에 새로운 속성 생성


#인스턴스 속성 생성
stu.score=95

#인스턴스 속성 확인
print(stu.name)
print(stu.score)


#is 연산자 예제

#인스턴스 생성해 대입
stu1=Student()
stu2=Student()

#stu1의 데이터를 대입 - stu1이 참조하고 있는 데이터 참조를 같이 참조
stu3=stu1

#인스턴스 동일성 확인
print(stu1==stu2) #내부 데이터 같은 지 확인 : False (인스턴스 별도 공간에 저장)
print(stu1 is stu2) #id 같은 지 확인 : False

print(stu1==stu3) #내부 데이터 같은 지 확인 : True
print(stu1 is stu3) #id 같은 지 확인 True

#getter, setter 예제
#이름과 점수 갖는 객체 여러개 필요
class NameScore:
    def getName(self):
        return self.name

    def setName(self,name):
        self.name=name

    def getScore(self):
        return self.score

    def setScore(self,score):
        self.score=score

namescore=NameScore()

#setter 이용한 속성 생성
namescore.setName("eunha")
namescore.setScore(10)

#getter 이용한 속성 사용
print(namescore.getName())
print(namescore.getScore())
