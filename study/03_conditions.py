# 파이썬 기초 3: 조건문

def grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "F"


for s in (95, 85, 72, 40):
    print(s, "->", grade(s))


def even_or_odd(n):
    return "짝수" if n % 2 == 0 else "홀수"


print(even_or_odd(7), even_or_odd(10))

# 윤년 판별
def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0


for y in (1900, 2000, 2024, 2026):
    print(y, "윤년" if is_leap(y) else "평년")
