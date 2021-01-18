first = int(input("첫 번째 과목의 점수를 입력하세요. :"))
second = int(input("두 번째 과목의 점수를 입력하세요. :"))
third = int(input("세 번째 과목의 점수를 입력하세요. :"))

total = first + second + third

average = int(total)/3

if total / 3 >= 60:
    print("평균점수는",average, "점으로 합격입니다.")

else: 
    print("평균점수는",average, "점으로 불합격입니다.")
    