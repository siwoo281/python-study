a = 0

while True:
    num = int(input("숫자를 입력하세요 : "))
    a += num

    if num == 0:
        print(a)
        break