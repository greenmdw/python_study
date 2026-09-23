# 파이썬 기초 8: 입출력과 간단한 계산기

def calculate(a, op, b):
    if op == "+":
        return a + b
    if op == "-":
        return a - b
    if op == "*":
        return a * b
    if op == "/":
        return a / b if b != 0 else "0으로 나눌 수 없음"
    return "알 수 없는 연산자"


for a, op, b in [(6, "+", 3), (6, "-", 3), (6, "*", 3), (6, "/", 3), (6, "/", 0)]:
    print(f"{a} {op} {b} = {calculate(a, op, b)}")

# input()은 문자열을 반환하므로 형변환이 필요하다
# age = int(input("나이: "))
raw = "25"
print(int(raw) + 1)
