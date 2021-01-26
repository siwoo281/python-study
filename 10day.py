num = int(input("정수를 입력하세요: "))
def total(N):
    return sum(n for n in range(1, N+1))

print(total(int(num)))