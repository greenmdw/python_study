# 파이썬 기초 9: 예외 처리


def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None
    finally:
        pass


def to_int(text):
    try:
        return int(text)
    except ValueError:
        print(f"'{text}'는 숫자가 아닙니다.")
        return 0


print(safe_divide(10, 2))
print(safe_divide(10, 0))
print(to_int("42"), to_int("abc"))

try:
    items = [1, 2, 3]
    print(items[5])
except IndexError as e:
    print("인덱스 오류:", e)

try:
    raise ValueError("직접 발생시킨 예외")
except ValueError as e:
    print(e)
