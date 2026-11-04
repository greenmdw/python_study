# 파이썬 기초 6: 리스트, 튜플, 딕셔너리, 집합

# 리스트
fruits = ["apple", "banana", "cherry"]
fruits.append("durian")
fruits.insert(1, "blueberry")
fruits.remove("banana")
print(fruits, len(fruits))
print(sorted(fruits), fruits[::-1])

nums = [5, 3, 8, 1, 9]
print(max(nums), min(nums), sum(nums))
print([n * n for n in nums if n > 3])

# 튜플 (변경 불가)
point = (3, 4)
x, y = point
print(x, y)

# 딕셔너리
person = {"name": "Charlie", "age": 30}
person["city"] = "Seoul"
for k, v in person.items():
    print(k, "=", v)
print(person.get("job", "없음"))

# 집합
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a | b, a & b, a - b)

# 글자 수 세기
word_count = {}
for ch in "hello world":
    if ch != " ":
        word_count[ch] = word_count.get(ch, 0) + 1
print(word_count)
