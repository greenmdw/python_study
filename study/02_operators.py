# 파이썬 기초 2: 연산자와 출력

a, b = 17, 5

print("더하기", a + b)
print("빼기", a - b)
print("곱하기", a * b)
print("나누기", a / b)
print("몫", a // b)
print("나머지", a % b)
print("제곱", a ** 2)

# 비교 / 논리 연산자
print(a > b, a == b, a != b)
print(a > 10 and b > 10)
print(a > 10 or b > 10)
print(not (a > b))

# 복합 대입 연산자
x = 10
x += 5
x *= 2
x -= 3
print("x =", x)

# 출력 옵션
print("A", "B", "C", sep="-")
print("줄바꿈 없음", end=" ")
print("이어서 출력")
print(f"{3.14159:.2f}", f"{1234567:,}", f"{7:03d}")
