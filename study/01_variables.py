# 파이썬 기초 1: 변수와 자료형

name = "Charlie"
age = 30
height = 175.5
is_student = True

print(name, type(name))
print(age, type(age))
print(height, type(height))
print(is_student, type(is_student))

# 형변환
num_str = "123"
num = int(num_str)
print(num + 1)
print(str(num) + "원")
print(float("3.14") * 2)

# 문자열 다루기
text = "Hello Python"
print(text.upper(), text.lower())
print(len(text), text[0], text[-1], text[0:5])
print(text.replace("Python", "World"))
print(f"{name}님은 {age}살입니다.")
