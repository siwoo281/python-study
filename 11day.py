nums = []
sum = 0
for i in range(7):
    num = int(input("정수를 입력 해주세요."))
    nums.append(num)

for i in range(7):
    sum = sum + nums[i]

average = sum / 7

print(average)
