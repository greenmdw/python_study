# 파이썬 기초 5: 함수


def add(a, b):
    return a + b


def greet(name, greeting="안녕하세요"):
    return f"{greeting}, {name}님!"


def total(*numbers):
    return sum(numbers)


def info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def fibonacci(n):
    a, b = 0, 1
    result = []
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result


print(add(3, 4))
print(greet("Charlie"))
print(greet("Charlie", greeting="Hello"))
print(total(1, 2, 3, 4, 5))
info(name="Charlie", age=30)
print(factorial(5))
print(fibonacci(10))

square = lambda x: x * x
print(list(map(square, [1, 2, 3, 4])))
