# This is a sample Python script.

#하나의 점수 입력받아 합/불합 결정
#가능성 있으면 예외처리 필요
try:
    score = int(input("Your score?: ").rstrip())

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
    print("올바른 점수 입력")

#프로그램 종료 문구
print("프로그램 종료")