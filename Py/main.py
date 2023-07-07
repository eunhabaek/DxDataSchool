# This is a sample Python script.

#if문 예시
#하나의 점수 입력받아 합/불합 결정
#예외처리 필요
try:
    score = int(input("Your score?: ").strip())

    if score >= 90 and score <= 100:
        print("A")
    elif score >= 80 and score < 90:
        print("B")
    elif score >= 70 and score < 80:
        print("C")
    elif score >= 60 and score < 70:
        print("D")
    elif score >= 0 and score < 60:
        print("F")
    else:
        print("바른 점수를 입력하세요.")
except:
    print("정수를 입력하세요.")

#프로그램 종료 문구
print("프로그램 종료")


#switch 유사구현 by dict
#0-6 요일로 출력
switcher={
    0:"sun",1:"mon",2:"tue",3:"wed",4:"thu",5:"fri",6:"sat"
}

try:
    num=int(input("요일을 위한 정수를 입력하세요: ").strip())
    print(switcher.get(num,"알 수 없는 요일"))
except:
    print("정수를 입력하세요.")


#if를 이용한 값 대입
x=9
y=False if x>9 else True
print(y)


#while문 예시

idx=0
while idx<10:
    print(idx)
    idx+=1
#반복문 모두 수행하고 종료된 경우 호출(break나 예외 발생시 수행 X)
else:
    print("while문 정상 종료됨")

#url page for로 만들기
page=0
url="http://www.donga.com/news/search?p="
for i in range(3):
    print(url,i*15+1,sep="")

#달력 찍기 (for문 1개로 쓰는게 포인트)
for i in range(1,32):
    print(i,end=" ")
    if i%7==0:
        print()

"""
i        j= 5-i => i 값으로 j 맞추기 => for문 한개
0 ***** 0-5
1 **** 0-4
2 *** 0-3
3 ** 0-2
4 * 0-1

"""
#별찍기 1
for i in range(5):
    for j in range(5-i):
        print("*",end="")

"""
*
**
***
**
*
"""

#별찍기 2
for i in range(5):
    if i<3:
        print("*"*(i+1))
    else:
        print("*" * (5-i))
"""
    *
   * *
  *   *
 *     *
*********

"""
#별찍기 3
for i in range(5):
    if i%4==0:
        print(" "*(4-i)+"*"*(2*i+1))
    else:
        print(" "*(4-i)+"*"+" "*(2*i-1)+"*")

#2부터 1000까지 완전수 개수
#완전수 =자신을 제외한 약수 합이 자신과 같은 수
def perf_num(n):
    cnt = 0
    for idx in range(2,n+1):
        perf_sum=1
        for i in range(2,idx//2+1):
            if idx%i==0:
                perf_sum+=i
        if perf_sum==idx:
            cnt+=1
    return cnt

print(perf_num(1000))


#피보나치 수열
#재귀로 하면 안됨, stack 너무 많이
def fibo0(n) -> int:
    if (n == 1) or (n == 2):
        return 1  # 코드1
    else:
        return (fibo0(n - 1) + fibo0(n - 2))

def fibo1(n):
    pivo_ls=[0]*(n)
    pivo_ls[0]=pivo_ls[1]=1
    for i in range(2,n):
        pivo_ls[i]=pivo_ls[i-1]+pivo_ls[i-2]
    return pivo_ls[n-1]

def fibo2(n):
    if n==1 or n==2:
        return 1
    else:
        n_1=1
        n_2=1
        result=0
        for i in range(3,n+1):
            result=n_1+n_2
            n_2=n_1
            n_1=result
        return result

print(dir(__builtins__))

#매개변수 자료형 기입, UML 표기법
def add(a:int,b:int)-> int:
    return a+b

print(add(3,4))

#call by value
def callByValue(a:int)->None:
    a=20
    print(a)

x=30

# scala는 값을 넘기므로 x값 변경 안됨
callByValue(x)
print(x)

#call by reference
def callByReference(ls:list)->None:
    ls[0]=20
    print(ls)

lst=[30,40,50]

# vector는 참조값을 넘기므로 lst값 변경
callByReference(lst)
print(lst)

# 매개변수의 unpacking
def collect(a,b):
    print(a)
    print(b)

col_dict={"a":10,"b":20}
#key 전달
collect(*col_dict)

#value 전달
collect(**col_dict)

#가변 매개변수
def merge(arg1,*arg2,arg3,**arg4):
    print(arg1)
    for elem in arg2:
        print(elem,end="")
    print()
    print(arg3)

    for elem2 in arg4:
        print(elem2,arg4[elem2])

merge(2,"1",20,"2",30,arg3=4,a=1,b=3)


#재귀함수
def hap(n:int)-> int:
    if n==1:
        return 1
    return n+hap(n-1)

print(hap(10))

#피보나치 수열 재귀로 =>메모리도 많이쓰고 오래걸림
import functools
@functools.lru_cache()

def fibonacci(n:'int>=1'=0)->int:
    fibonacci.__doc__ = "재귀 이용하여 피보나치 수열 값 리턴하는 함수"
    if n==1 or n==2:
        return 1
    return fibonacci(n-2)+fibonacci(n-1)

print(fibonacci(5))
help(fibonacci)

def dragonAttack():
    print("드래곤의 공격")
def tankAttack():
    print("탱크의 공격")

#다형성
delegate=dragonAttack()
delegate()
delegate=tankAttack()
delegate()

#high order function
def outer():
    def inner():
        print("내부 함수")
    return inner

f1=outer()
f1()


#하노이의 탑 실습

