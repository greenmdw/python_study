# 파이썬 기초 4: 반복문

# for + range
for i in range(1, 6):
    print(i, end=" ")
print()

# 1부터 100까지 합
total = 0
for i in range(1, 101):
    total += i
print("합계:", total)

# 구구단 3단
for i in range(1, 10):
    print(f"3 x {i} = {3 * i}")

# while
n = 1
while n <= 32:
    print(n, end=" ")
    n *= 2
print()

# break / continue
for i in range(1, 11):
    if i % 2 == 0:
        continue
    if i > 7:
        break
    print("홀수:", i)

# 별 찍기
for i in range(1, 5):
    print("*" * i)
