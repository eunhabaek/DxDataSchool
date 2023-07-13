# 접근자 메서드
#클래스 생성
class Animals():

    #생성자 - 인스턴스 생성할 때 호출
    def __init__(self,name="noname"): #속성에 대입할 매개변수="기본 값"
        print("인스턴스 생성")

        #생성자 안에 속성 생성하면 처음부터 속성 소유 가능

        self.default="기본 값" #default 값은 "기본 값"으로 밖에 초기화 안 됨
        self.name=name #매개변수 이용해서 속성 다르게 대입 가능

    #소멸자 - 인스턴스 삭제될 때 호출
    def __del__(self):
        print("인스턴스 소멸")

    def display(self): #메서드의 첫번째 매개변수는 기본적으로 self이며 실제 호출할 땐 생략
        print("인스턴스 메서드 출력") #인스턴스 없이는 호출 불가


anm=Animals("cat") #인스턴스 생성, 참조 카운트 1

#메서드 호출
Animals.display(anm) #unbound 호출
anm.display() #bound 호출

print(anm.name)

anm=None #인스턴스 소멸되어 소멸자 호출




#일련번호 인스턴스 생성
class Nums():
    # 클래스 속성
    auto_increment = 0

    # 클래스 속성과 생성자를 이용한 일련번호
    def __init__(self):
        Nums.auto_increment+=1
        self.no=Nums.auto_increment

    @staticmethod #인스턴스 만들 필요 없음
    def staticmd():
        print("static method")

    @classmethod
    def classmd(cls):
        print(cls.auto_increment)


num1=Nums()
print(num1.no) #1 출력

num2=Nums()
print(num2.no) #2 출력

#static method 호출
Nums.staticmd()

#class method 호출
Nums.classmd()


#reference count 확인
import sys
print(sys.getrefcount(num1))


#속성 생성제한, 연산자 오버로딩
class Blank:
    #name과 age, __no 속성만 사용 가능하도록
    __slots__=["name","age","__no"]
    def __init__(self,name):
        self.name=name
        self.__no=1 #private 속성, 메서드 통해서만 접근 가능

    #연산자 overloading
    def __add__(self,other):
        return self.name+other.name

    def __eq__(self, other):
        return self.name==other.name

bnk1=Blank("eunha")
bnk2=Blank("eunha")
bnk3=bnk1

print(bnk1+bnk2) # 오버로딩 하지 않으면 에러

print(bnk1==bnk2) #원래 false이나, 오버로딩으로 인해 true
print(bnk1 is bnk2) #false

print(bnk1==bnk3) #true
print(bnk1 is bnk3) #ture

#생성 제한
bnk.name="eunha"
bnk.age=27
#bnk.job="student" #에러남, 변수 제한
#print(bnk.__no) #에러남, private

#property 직접 작성

class Prop1:
    def __init__(self,name="noname"):
        self.__name=name
        self.age=27

    #접근자 메서드
    def getName(self):
        print("name의 getter 호출")
        return self.__name

    def setName(self,name):
        print("name의 setter 호출")
        self.__name=name

    #property 생성
    #name 호출하면 getName 메서드 호출, name 값 대입하면 setName 메서드 호출
    #name=property(fget=getName, fset=setName)


pro1=Prop1()

print(pro1.age)
print(pro1.__name)

#property 이용한 getter setter 호출
pro1.name="eunha"
print(pro1.name)



#property decorator 이용
class Prop2:
    def __init__(self,name="noname"):
        self.__name=name

    #접근자 메서드
    @property
    def name(self):
        print("name의 getter 호출")
        return self.__name
    @name.setter
    def name(self,name):
        print("name의 setter 호출")
        self.__name=name

pro2=Prop2()

#property 이용한 getter setter 호출
pro2.name="eunha"
print(pro2.name)

#상속 예시

class Sup:
    def __init__(self):
        self.name="noname"
    def method(self):
        print("상위 클래스의 메서드")

class Sub(Sup):
    #하위 클래스에서
    def __init__(self):
        super().__init__() #상속에서 중요함
        self.score=80
    def method(self): #메서드 오버라이딩
        super().method() #상위 클래스의 메서드 호출
        print("메서드 오버라이딩")

    def subMethod(self):
        print("하위 클래스의 메서드")

#sub의 인스턴스 생성해서 필요한 메서드 호출
sub=Sub()
sub.subMethod()
sub.method()
print(sub.name)


#추상 클래스 생성
import abc
class AbstractClass(metaclass=abc.ABCMeta):
    #추상 메서드 - 내용 없음, 하위 클래스에서 구현하여 사용
    @abc.abstractmethod
    def method(self):
        pass

#추상클래스 상속０
class Sub(AbstractClass):
    def __init__(self):
        print('인스턴스 생성')
    def method(self): #추상 메서드 반드시 implementation 해야함
        print("추상 메서드 구현")

#instance=AbstractClass() #추상클래스는 인스턴스 생성 불가
instance=Sub() #추상클래스 implementation 하지 않으면 에러
instance.method()


import sys #모듈 추가
print(sys.modules)#사용 가능 모듈 확인
print(sys.path)#모듈 경로 확인
#sys.path.append("추가할 path") --> 환경변수 path 추가 가능

#다른 파일로 모듈 만들어서 불러오기
import mymath
sys.path.append("./") #현재 디렉토리에서 모듈이나 패키지를 import
mymath.func("Hello")


#matplotlib 패키지 이용
import matplotlib.pyplot as plt

#boxplot 그리기
fig=plt.figure(figsize=(10,7))
plt.boxplot([1,2,3,4],[4,3,2,1])
plt.grid()
plt.show()
fig.savefig("plt.png")

#수학관련 모듈 이용
#decimal.Decimal()
from decimal import Decimal

#실수 계산 에러(머신 엡실론) 줄일 수 있음
print(0.2==(1.0-0.8)) #False
print(Decimal("0.2")==(Decimal("1.0")-Decimal("0.8"))) #True

#import random
import random
import time

#help(random.choice)

mynumber=list(map(int,input("1부터 45까지의 정수를 공백 구분하여 6개 입력하세요: ").split()))
mynumber.sort()

print("내가 선택한 6개 로또 번호: ",mynumber)

random.seed(42)

for i in range(n):
    time.sleep(1)
    lotto=random.sample(range(1,46),6)
    lotto.sort()
    print(i+1,"번째 당첨번호",lotto)
    if lotto==mynumber:
        print("로또 당첨!",i)
    else:
        print("다음 기회에!")
    print()


#리스트 데이터 랜덤하게 확장하기?
